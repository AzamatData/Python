# Homework 1:
import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df
# 1.	Rename column names using function. "First Name" --> "first_name", "Age" --> "age
def change_columns_name(df, columns_map):
    return df.rename(columns=columns_map)
columns_name_to_change={"First Name":"first_name", "Age":"age"}
df = change_columns_name(df, columns_name_to_change)
print(df)
# 2.	Print the first 3 rows of the DataFrame
print(df.head(3))
# 3.	Find the mean age of the individuals
print(df['age'].mean())
# 4.	Select and print only the 'Name' and 'City' columns
print(df[['first_name', 'City']])
# 5.	Add a new column 'Salary' with random salary values
df['Salary']=0
print(df)
# 6.	Display summary statistics of the DataFrame
print(df.describe())
