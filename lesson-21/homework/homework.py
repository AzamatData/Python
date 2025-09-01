# Homework:
# DataFrame 1: Student Grades
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.

average_grade = df1[['Student_ID', 'Math', 'English', 'Science']]
average_grade['Average'] = average_grade[['Math', 'English', 'Science']].mean(axis=1)
average_grade
# Exercise 2: Find the student with the highest average grade.

top_average = average_grade.loc[average_grade['Average'].idxmax()]
top_average
# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
average_grade['Total'] = average_grade[['Math', 'English', 'Science']].sum(axis=1)
average_grade

# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
from matplotlib import pyplot as plt
subject_means = df1[['Math', 'English', 'Science']].mean()

subject_means.plot(kind='bar', color='green', figsize=(6,4))

plt.title('Average Grades per Subject')
plt.ylabel('Average Grade')
plt.xlabel('Subject')
plt.xticks(rotation=0)   
plt.show()

# DataFrame 2: Sales Data
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

df2

# Exercise 1: Calculate the total sales for each product.
df2['Total'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)

# Exercise 2: Find the date with the highest total sales.

highest_total = df2.loc[df2['Total'].idxmax()]
highest_total

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
df2[['Product_A_pct', 'Product_B_pct', 'Product_C_pct']] = df2[['Product_A','Product_B','Product_C']].pct_change() * 100
df2
# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
import matplotlib.pyplot as plt

df2.set_index('Date')[['Product_A','Product_B','Product_C']].plot(figsize=(8,5))

plt.title('Sales Trends for Each Product')
plt.ylabel('Sales')
plt.xlabel('Date')
plt.legend(title='Product')
plt.grid(True)
plt.show()

# DataFrame 3: Employee Information
import pandas as pd
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.
average_salary = df3.groupby('Department')['Salary'].mean()
average_salary
# Exercise 2: Find the employee with the most experience.
most_experience = df3.loc[df3['Experience (Years)'].idxmax()]
most_experience
# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
min_sal = df3['Salary'].min()

df3['Salary Increase'] = ((df3['Salary']-min_sal)/min_sal) *100

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
import matplotlib.pyplot as plt

dept_counts = df3['Department'].value_counts()

dept_counts.plot(kind='bar', color='skyblue', figsize=(6,4))
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.show()

# DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
df4
# Exercise 1: Calculate the total revenue from all orders.
# total_revenue = df4['Total_Price'].sum()
# total_revenue

# Exercise 2: Find the most ordered product.
# grouped_product = df4.loc[df4.groupby('Product')['Total_Price'].sum().idxmax()]
grouped_product = df4.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
most_ordered = grouped_product.idxmax()
most_quantity =  grouped_product.max()
print(f"The most ordered product is {most_ordered} with {most_quantity} units.")

# Exercise 3: Calculate the average quantity of products ordered.
average_quantity = df4.groupby('Product')['Quantity'].mean().reset_index()
average_quantity
# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
import matplotlib.pyplot as plt


sales_by_product = df4.groupby('Product')['Total_Price'].sum()


plt.figure(figsize=(6,6))
plt.pie(
    sales_by_product,
    labels=sales_by_product.index,
    autopct='%1.1f%%',   
    startangle=140
)
plt.title("Distribution of Sales Across Products")
plt.show()


