# Homework Assignment 1: Analyzing Sales Data
# You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:
# •	Date: Date of the sale.
# •	Product: Name of the product sold.
# •	Category: Category to which the product belongs.
# •	Quantity: Number of units sold.
# •	Price: Price per unit.
# Tasks:
# 1.	Group the data by the Category column and calculate the following aggregate statistics for each category:
# o	Total quantity sold.
# o	Average price per unit.
# o	Maximum quantity sold in a single transaction.
import pandas as pd
sales_data_df = pd.read_csv('task/sales_data.csv')
groupby_category = sales_data_df.groupby('Category') 
groupby_category.agg({'Quantity': 'sum', 'Price': 'mean', 'Quantity': 'max'})

groupby_category.agg(Total_quantity_sold = ('Quantity', 'sum'), average_price_per_unit = ('Price', 'mean'), maximum_quantity_sold = ('Quantity', 'max'))

# 2.	Identify the top-selling product in each category based on the total quantity sold.
# sales_data_df
product_group = sales_data_df.groupby(['Category', 'Product']).sum().reset_index()
product_group['Rank'] = product_group.groupby('Category')['Quantity'].rank(method='first',ascending=False)

top_selling = product_group[product_group['Rank']==1]
top_selling

# 3.	Find the date on which the highest total sales (quantity * price) occurred.
sales_data_df['total_sales'] = sales_data_df['Quantity']*sales_data_df['Price']
groped_total_sales = sales_data_df.groupby('Date')['total_sales'].sum().reset_index()

highest_total_sales =groped_total_sales.loc[[groped_total_sales['total_sales'].idxmax()]]
highest_total_sales

# Homework Assignment 2: Examining Customer Orders
# You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:
# •	OrderID: Unique identifier for each order.
# •	CustomerID: Unique identifier for each customer.
# •	Product: Name of the product ordered.
# •	Quantity: Number of units ordered.
# •	Price: Price per unit.
# Tasks:
# 1.	Group the data by CustomerID and filter out customers who have made less than 20 orders.
import pandas as pd
customer_order_df = pd.read_csv('task/customer_orders.csv')

# grouped_customerid = customer_order_df.groupby('CustomerID')['Quantity'].sum().reset_index()
# grouped_customerid = grouped_customerid['Quantity']<20
# customer_order_df[grouped_customerid]


low_quantity_customers = (
    customer_order_df.groupby('CustomerID')['Quantity']
    .sum()
    .reset_index()
    .query('Quantity < 20')['CustomerID']
)


result = customer_order_df[customer_order_df['CustomerID'].isin(low_quantity_customers)]

print(result)

# 2.	Identify customers who have ordered products with an average price per unit greater than $120.

grouped_customerid = customer_order_df.groupby('CustomerID')['Price'].mean().reset_index()
res = grouped_customerid[grouped_customerid['Price']>120]
res

# 3.	Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
customer_order_df['Quantity'] = pd.to_numeric(customer_order_df['Quantity'], errors='coerce')
customer_order_df['Price'] = pd.to_numeric(customer_order_df['Price'], errors='coerce')

customer_order_df['LinePrice'] = customer_order_df['Quantity']*customer_order_df['Price']

group_each_product = (customer_order_df.groupby('Product')
                      .agg(
                          total_quantity = ('Quantity', 'sum'),
                          total_price = ('LinePrice', 'sum')
                      ).reset_index()
                      )
result = group_each_product[group_each_product['total_quantity']<5]
result


# Homework Assignment 3: Population Salary Analysis
# 1.	"task\population.db" sqlite database has population table.
import sqlite3
import pandas as pd


con = sqlite3.connect("../Class19/task/population.db")
df = pd.read_sql_query("SELECT * from population", con)

con.close()
# df['Salary_Band'] = df

def categorize_values(row):
    if row['salary'] <200000:
        return 'till $200,000'
    elif row['salary']>200001 and row['salary']<400000:
        return '$200,001 - $400,000'
    elif row['salary']>400001 and row['salary']<600000:
        return '$400,001 - $600,000'
    elif row['salary']>600001 and row['salary']<800000:
        return '$600,001 - $800,000'
    elif row['salary']>800001 and row['salary']<1000000:
        return '$800,001 - $1,000,000'
    elif row['salary']>1000001 and row['salary']<1200000:
        return '$1,000,001 - $1,200,000'
    elif row['salary']>1200001 and row['salary']<1400000:
        return '$1,200,001 - $1,400,000'
    elif row['salary']>1400001 and row['salary']<1600000:
        return '$1,400,001 - $1,600,000'
    elif row['salary']>1600001 and row['salary']<1800000:
        return '$1,600,001 - $1,800,000'
    else: 
        return '$1,800,001 and over'


# Apply the function to create the new column
df['Salary_Band'] = df.apply(categorize_values, axis= 1)
df

# 2.	"task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# o	Percentage of population for each salary category;
# o	Average salary in each salary category;
# o	Median salary in each salary category;
# o	Number of population in each salary category;
all_population = df['id'].count()

group_each_category = (df.groupby('Salary_Band')
                      .agg(
                          avarage_salary = ('salary', 'mean'),
                          median_salary = ('salary', 'median'),
                          number_of_population = ('id', 'count')

                      ).reset_index()
                      )
group_each_category['in_percentage'] = (
    group_each_category['number_of_population'] / all_population * 100)
group_each_category
# exl_df = pd.read_excel("../Class19/task/population_salary_analysis.xlsx")
# exl_df
# 3.	Calculate the same measures in each State
result_by_state_band = (
    df.groupby(['state','Salary_Band'])
      .agg(
          in_percentage=('id', lambda x: len(x)/all_population*100),
          average_salary=('salary', 'mean'),
          median_salary=('salary', 'median'),
          number_of_population=('id', 'count')
      )
      .reset_index()
)
result_by_state_band
# df
# Note: Use SQL only to select data from database. All the other calculations should be done in python.
