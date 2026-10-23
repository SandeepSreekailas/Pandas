#merge() vs concat()
''' 
merge() — Combine using a common column
concat() — Combine DataFrames together
'''

#Merge
#DataFrame 1 — Employees
import pandas as pd

employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Arun", "Binu", "Charan"]
})

#DataFrame 2 — Salaries
salaries = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Salary": [15000, 25000, 18000]
})

# result=pd.merge(employees, salaries, on="EmpID")
# print(result)

# Types of merge
'''
Merge type	What it does
inner	Keeps only matching IDs
left	Keeps every row from the left DataFrame
right	Keeps every row from the right DataFrame
outer	Keeps all IDs from both DataFrames

inner is the default merge type.
'''
# a=pd.merge(employees, salaries, on="EmpID", how="inner")
# print(a)
# b=pd.merge(employees, salaries, on="EmpID", how="left")
# print(b)
# c=pd.merge(employees, salaries, on="EmpID", how="outer")
# print(c)


#concat()
#A. Vertical concatenation (rows)
df1 = pd.DataFrame({
    "Name": ["Arun", "Binu"],
    "Salary": [15000, 25000]
})

df2 = pd.DataFrame({
    "Name": ["Charan", "Deepa"],
    "Salary": [18000, 35000]
})

result = pd.concat([df1, df2], ignore_index=True)
# print(result)
'''
ignore_index=True creates a fresh index: 0, 1, 2, 3.
'''

# B. Horizontal concatenation (columns)
df1 = pd.DataFrame({"Name": ["Arun", "Binu"]})
df2 = pd.DataFrame({"Salary": [15000, 25000]})

result = pd.concat([df1, df2], axis=1)
print(result)
'''
axis=1 places columns side by side. Pandas aligns rows by their index, not by a matching employee ID.
'''

'''
merge()

Combines data by matching values in a key column, like EmpID.

Think: match related records.

concat()

Combines DataFrames by stacking rows or placing columns side by side.

Think: join datasets together.
'''