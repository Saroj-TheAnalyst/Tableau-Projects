from datetime import datetime
from pathlib import Path
import pandas as pd
import plotly.express as px
from faicons import icon_svg
from shinywidgets import render_plotly
from shiny import reactive
from shiny.express import input, render, ui
from state_choices import STATE_CHOICES

# ---------------------------------------------------------------------
# Reading in Files
# ---------------------------------------------------------------------
def load_data(file_name):
    file_path = Path(__file__).parent / file_name
    return pd.read_csv(file_path)

new_listings_df = load_data("Metro_new_listings_uc_sfrcondo_sm_month.csv")
median_listing_price_df = load_data("Metro_mlp_uc_sfrcondo_sm_month.csv")
for_sale_inventory_df = load_data("Metro_invt_fs_uc_sfrcondo_sm_month.csv")

# ---------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------
def string_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def filter_by_date(df: pd.DataFrame, date_range: tuple):
    rng = sorted(date_range)
    dates = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.date
    return df[(dates >= rng[0]) & (dates <= rng[1])]

# ---------------------------------------------------------------------
# UI Setup
# ---------------------------------------------------------------------
ui.page_opts(title="US Housing App")

with ui.sidebar():
    ui.input_select("state", "Filter by State", choices=STATE_CHOICES)
    ui.input_slider("date_range", "Filter by Date Range",
                    min=string_to_date("2018-03-31"),
                    max=string_to_date("2024-04-30"),
                    value=[string_to_date("2018-03-31"), string_to_date("2024-04-30")])

# ---------------------------------------------------------------------
# Current Median List Price Box
# ---------------------------------------------------------------------
with ui.layout_column_wrap():
    with ui.value_box(showcase=icon_svg("dollar-sign")):
        "Current Median List Price"

        @render.ui
        def price():
            date_columns = median_listing_price_df.columns[6:]
            states = median_listing_price_df.groupby("StateName").mean(numeric_only=True)
            dates = states[date_columns].reset_index()
            states = dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")

            df = states[states["StateName"] == input.state()] if input.state() != "United States" else states
            last_value = df.iloc[-1, -1]
            return f"${last_value:,.0f}"

# ---------------------------------------------------------------------
# Home Inventory % Change Box
# ---------------------------------------------------------------------
    with ui.value_box(showcase=icon_svg("house")):
        "Home Inventory % Change"

        @render.ui
        def change():
            date_columns = for_sale_inventory_df.columns[6:]
            states = for_sale_inventory_df.groupby("StateName").mean(numeric_only=True)
            dates = states[date_columns].reset_index()
            states = dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")

            df = states[states["StateName"] == input.state()] if input.state() != "United States" else states
            last_value, second_last_value = df.iloc[-1, -1], df.iloc[-2, -1]
            percentage_change = ((last_value - second_last_value) / second_last_value * 100)
            sign = "+" if percentage_change > 0 else "-"
            return f"{sign}{abs(percentage_change):.2f}%"

# ---------------------------------------------------------------------
# Median List Price Visualizations
# ---------------------------------------------------------------------
with ui.navset_card_underline(title="Median List Price"):
    with ui.nav_panel("Plot", icon=icon_svg("chart-line")):
        @render_plotly
        def list_price_plot():
            date_columns = median_listing_price_df.columns[6:]
            price_grouped_dates = median_listing_price_df.groupby("StateName")[date_columns].mean().reset_index()
            df = price_grouped_dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")
            df = filter_by_date(df, input.date_range())
            df = df if input.state() == "United States" else df[df["StateName"] == input.state()]

            fig = px.line(df, x="Date", y="Value", color="StateName")
            fig.update_xaxes(title_text="")
            fig.update_yaxes(title_text="")
            return fig

    with ui.nav_panel("Table", icon=icon_svg("table")):
        @render.data_frame
        def list_price_data():
            df = median_listing_price_df if input.state() == "United States" else median_listing_price_df[median_listing_price_df["StateName"] == input.state()]
            return render.DataGrid(df)

# ---------------------------------------------------------------------
# Home Inventory Visualizations
# ---------------------------------------------------------------------
with ui.navset_card_underline(title="Home Inventory"):
    with ui.nav_panel("Plot", icon=icon_svg("chart-line")):
        @render_plotly
        def for_sale_plot():
            date_columns = for_sale_inventory_df.columns[6:]
            for_sale_grouped_dates = for_sale_inventory_df.groupby("StateName")[date_columns].sum().reset_index()
            df = for_sale_grouped_dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")
            df = filter_by_date(df, input.date_range())
            df = df if input.state() == "United States" else df[df["StateName"] == input.state()]

            fig = px.line(df, x="Date", y="Value", color="StateName")
            fig.update_xaxes(title_text="")
            fig.update_yaxes(title_text="")
            return fig

    with ui.nav_panel("Table", icon=icon_svg("table")):
        @render.data_frame
        def for_sale_data():
            df = for_sale_inventory_df if input.state() == "United States" else for_sale_inventory_df[for_sale_inventory_df["StateName"] == input.state()]
            return render.DataGrid(df)

# ---------------------------------------------------------------------
# New Listings Visualizations
# ---------------------------------------------------------------------
with ui.navset_card_underline(title="New Listings"):
    with ui.nav_panel("Plot", icon=icon_svg("chart-line")):
        @render_plotly
        def listings_plot():
            date_columns = new_listings_df.columns[6:]
            new_listings_grouped_dates = new_listings_df.groupby("StateName")[date_columns].sum().reset_index()
            df = new_listings_grouped_dates.melt(id_vars=["StateName"], var_name="Date", value_name="Value")
            df = filter_by_date(df, input.date_range())
            df = df if input.state() == "United States" else df[df["StateName"] == input.state()]

            fig = px.line(df, x="Date", y="Value", color="StateName")
            fig.update_xaxes(title_text="")
            fig.update_yaxes(title_text="")
            return fig

    with ui.nav_panel("Table", icon=icon_svg("table")):
        @render.data_frame
        def listings_data():
            df = new_listings_df if input.state() == "United States" else new_listings_df[new_listings_df["StateName"] == input.state()]
            return render.DataGrid(df)
