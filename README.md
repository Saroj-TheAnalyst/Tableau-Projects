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

---

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

