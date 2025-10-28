import numpy as np
import pandas as pd

# Creating series in pandas

# labels = ['a','b','c']
# my_list = [10,20,30]
# arr = np.array({10,20,30})
# d = {1:10,2:20,3:30}

# print(pd.Series(my_list))

# Dataframes

# data = {
#     'Name':['John','Peter'],
#     'Age' : [28,34],
#     'City' : ['Paris','Berlin'],
#     'Salary' : [1200,3400]
# }

# df = pd.DataFrame(data)
# print(df)

# df['Designation'] = ['Doctor','Engineer']
# print(df)

# print(df.drop('Designation',axis=1,inplace=True))

# print(df)

# print(df.loc[[0,1]][['Name','Age']])

# print(df[(df['City']== 'Paris')])

# Find missing data

# data = {
#     'A':[1,2,np.nan,4,5],
#     'B':[np.nan,2,3,4,5],
#     'C':[1,2,3,np.nan,np.nan],
#     'D':[1,np.nan,np.nan,np.nan,5],
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.fillna(0))

# values = {'A':1,'B':2,'C':3,'D':4}
# print(df.fillna(value=values))


# merging 2 dataframes

# employees = pd.DataFrame({
#     'employee_id':[1,2,3,4,5],
#     'name': ['John','Anna','Peter','Linda','Rob'],
#     'department':['HR','IT','Finance','IT','HR']
# })

# salaries = pd.DataFrame({
#     'employee_id':[1,2,3,6,7],
#     'salary':[60000,80000,65000,70000,90000],
#     'bonus':[5000,10000,7000,8000,12000]
# })

# print(pd.merge(employees,salaries,on='employee_id',how='left'))


# Group by

# data = {
#     'Category' : ['A','B','A','B','A','B','A','B'],
#     'Store' : ['S1','S1','S2','S2','S1','S2','S2','S1'],
#     'Sales' : [100,200,150,250,120,180,200,300],
#     'Quantity' : [10,15,12,18,8,20,15,25],
#     'Date' : pd.date_range('2023-01-01',periods=8)
# }

# df = pd.DataFrame(data)
# print(df)

# Group by category and calculate the sum of sales

# cat = df.groupby('Category')['Sales'].sum()
# print(cat)

# for i,v in cat:
#     print(i)
#     print(v)


# Group by store and sum of sales

# store = df.groupby('Store')['Sales'].sum()
# print(store)


# Aggregation

# aggregation = df['Sales'].agg(['mean','median','min','max','sum','count','std'])
# print(aggregation)


# Pivot tables

data = {
    'Date' : pd.date_range('2023-01-01',periods=20),
    'Product' : ['A','B','C','D'] * 5,
    'Region' : []
}