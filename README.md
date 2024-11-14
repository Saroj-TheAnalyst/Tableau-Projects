# Tableau Dashboard Tutorial 2024

## Overview

This repository provides a comprehensive Tableau dashboard tutorial for beginners. The project demonstrates the process of building interactive and insightful visualizations using Tableau, starting from data preparation and ending with publishing your dashboard. Whether you are a beginner or an intermediate user, this guide will help you learn how to connect to data, create various types of visualizations, and create interactive dashboards.

---

## Prerequisites

- **Tableau Desktop**: Install Tableau Desktop from the [official website](https://www.tableau.com/products/desktop).
- **SQL Database**: A basic understanding of SQL queries. You will connect to a sample SQL database containing sales and customer data.
  ---

## Step 1: Connecting to Data

1. Open Tableau Desktop and click **"Connect to Data"**.
2. Select the data source you want to connect to, such as **Excel**, **CSV**, or a **SQL database**.
3. For SQL, enter your server details and credentials:
   - **SQL Sample Query**:
     ```sql
     SELECT 
         OrderID, 
         ProductName, 
         Sales, 
         Profit, 
         OrderDate, 
         CustomerName, 
         Region
     FROM Orders
     ```
4. Click **Connect** to establish the data connection.


## Step 2: Data Preparation in Tableau

1. **Data Interpreter**: Tableau automatically detects and cleans up data formatting issues.
2. **Joining Tables**: If needed, join multiple tables to get a unified dataset. For example:
   ```sql
   SELECT 
       o.OrderID, 
       o.ProductName, 
       o.Sales, 
       o.Profit, 
       c.CustomerName, 
       c.Region
   FROM Orders o
   JOIN Customers c
   ON o.CustomerID = c.CustomerID

3. **Calculated Fields**: Create calculated fields to enhance your analysis. For example, calculating Profit Margin:
Profit Margin: (Profit / Sales) * 100
4. **Filters**: Apply filters to display relevant data, such as filtering by region or product category.

## Step 3: Create Your First Visualization

1. **Line Chart for Sales Over Time**:
    - Drag **OrderDate** to the **Columns** shelf.
    - Drag **Sales** to the **Rows** shelf.
    - This will automatically create a **line chart** that displays sales over time.
  
2. **Change Aggregation**:
    - By default, Tableau aggregates data in a summary form (SUM, AVG, etc.).
    - Right-click the **Sales** field in the **Rows** shelf, and choose **Measure (Sum)** → **Average** or any other aggregation that fits your needs.
  
3. **Exploring Chart Types**:
    - Use the **Show Me** panel to experiment with different chart types like **bar charts**, **scatter plots**, **pie charts**, and more. This allows you to visualize data in different ways and select the most effective type for your dataset.

---

## Step 4: Create Multiple Visualizations

1. **Bar Chart for Sales by Region**:
    - Drag **Region** to the **Rows** shelf.
    - Drag **Sales** to the **Columns** shelf.
    - This creates a **bar chart** that shows sales by region.

2. **Scatter Plot for Sales vs. Profit**:
    - Drag **Sales** to the **Columns** shelf.
    - Drag **Profit** to the **Rows** shelf.
    - A scatter plot will appear showing the relationship between sales and profit.
    - **Add Customer Information**: Drag **CustomerName** to the **Detail** shelf for more granular insight.

---

## Step 5: Build a Dashboard

Once you’ve created several visualizations, you can combine them into a single, interactive dashboard.

1. **Creating a New Dashboard**:
    - Click the **Dashboard** tab at the bottom and select **New Dashboard**.
    - You can also use the shortcut **Ctrl + D** (Windows) or **Cmd + D** (Mac).
  
2. **Adding Sheets to the Dashboard**:
    - On the left panel, you'll see the different visualizations (sheets) you’ve created.
    - Drag the individual sheets from the left panel to the dashboard area.
    - Resize and adjust each sheet’s layout to fit your design needs. You can place sheets side by side or stack them based on the dashboard’s purpose.

---

## Step 6: Add Interactivity

1. **Filter Action**:
    - Click **Dashboard** → **Actions** → **Add Action** → **Filter**.
    - Choose a **Source Sheet** (e.g., a bar chart showing sales by region) and a **Target Sheet** (e.g., the line chart showing sales over time).
    - This will allow you to filter the data shown on the sales chart by clicking on a region in the bar chart.

2. **Highlight Action**:
    - Click **Dashboard** → **Actions** → **Add Action** → **Highlight**.
    - This will highlight related data across all visualizations when you hover or click on specific data points. For example, hovering over a specific customer name will highlight the related data points across all charts.

---

## Step 7: Customize the Appearance

1. **Color Adjustments**:
    - Customize the color schemes in your visualizations to make them more visually appealing.
    - Right-click the **Sales** field in the **Rows** shelf and select **Edit Colors** to choose from a range of color palettes.
  
2. **Add Titles and Labels**:
    - Titles help provide context to your visualizations. You can add titles by clicking on the **Title** option in the **Worksheet** menu.
    - You can also add labels to the data points in your chart by dragging the **Sales** or **Profit** field to the **Label** shelf.

3. **Customize Tooltips**:
    - Tooltips appear when you hover over a data point. You can customize the tooltips to show more or less data by clicking on **Tooltip** in the **Marks** card.
    - For example, you can show additional details such as profit margins, customer names, and more.

---

## Step 8: Publish Your Dashboard

1. **Save the Workbook**:
    - Save the workbook by going to **File** → **Save As**. You can save it in either `.twb` (Tableau Workbook) or `.twbx` (Tableau Packaged Workbook) formats.
    - A `.twbx` file includes both the workbook and the data source, making it easier to share with others.

2. **Publish to Tableau Server or Tableau Online**:
    - If you have access to **Tableau Server** or **Tableau Online**, you can publish your workbook directly there.
    - Go to **Server** → **Tableau Server/Online** → **Sign In**.
    - After signing in, click on **Publish Workbook** to make your dashboard available online.

3. **Export as PDF or Image**:
    - If you need to share your dashboard in a static format, you can export it as a PDF or image.
    - Go to **File** → **Export** → **Export as Image** or **Export as PDF**.
  
4. **Upload to Tableau Public**:
    - If you want to share your dashboard publicly, you can upload it to **Tableau Public**.
    - Go to **Server** → **Tableau Public** → **Save to Tableau Public**.
    - You’ll need a Tableau Public account to upload your work.

---

## Conclusion

This tutorial provided a step-by-step guide to building a comprehensive Tableau dashboard. By following the outlined steps, you should now have a solid understanding of the Tableau process, from connecting to your data, creating various types of visualizations, adding interactivity, and publishing your dashboard for sharing and analysis.

### Key Takeaways:
- **Data Connection**: Learn how to connect to SQL databases and clean your data using Tableau.
- **Creating Visualizations**: Master different types of visualizations such as line charts, bar charts, and scatter plots.
- **Interactive Dashboards**: Combine visualizations into a single dashboard and add actions like filtering and highlighting.
- **Customization**: Customize the appearance of your visualizations with colors, titles, and tooltips.
- **Publishing**: Publish and share your dashboard via Tableau Server, Tableau Online, or Tableau Public.

---

## Resources

- [Tableau Documentation](https://www.tableau.com/support/help)
- [Tableau Public Gallery](https://public.tableau.com/en-us/gallery/)
- [SQL Tutorial for Beginners](https://www.w3schools.com/sql/)

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## Acknowledgements

Special thanks to the Tableau community and resources for providing tools and examples to help create this tutorial. Additionally, thank you to all the contributors who helped make Tableau accessible to all users, regardless of their skill level.

