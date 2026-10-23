# groupby() and aggregation

import pandas as pd

data = {
    "Name": ["Arun", "Binu", "Charan", "Deepa", "Eva"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [15000, 25000, 18000, 35000, 22000]
}

df = pd.DataFrame(data)
'''
What does groupby() do?
Imagine you have this DataFrame:

Suppose you want to calculate the average salary of each department.
Without groupby(), you'd have to filter each department separately. With groupby(), it's simple:
'''
# r=df.groupby("Department")["Salary"].mean()
# print(r)

'''
Method	Meaning
.sum()	Total
.mean()	Average
.count()	Count non-missing values
.min()	Minimum
.max()	Maximum
.size()	Number of rows in each group
'''

# Total salary by department
# r=df.groupby("Department")["Salary"].sum()
# print(r)

# Highest salary by department
# r=df.groupby("Department")["Salary"].max()
# print(r)

# Number of employees in each department
# r=df.groupby("Department").size()
# print(r)

#Multiple aggregations with agg()
# r=df.groupby("Department")["Salary"].agg(
#     ["mean", "max", "min", "sum"]
# )
# print(r)

# Aggregate different columns separately
# r=df.groupby("Department").agg(
#     {
#         "Salary":["mean","max"],
#         "Name":"count"
#     }
# )
# print(r)