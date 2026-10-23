# Filtering and Sorting
import pandas as pd

data = {
    "Name": ["Arun", "Binu", "Charan", "Deepa", "Eva"],
    "Age": [22, 25, 21, 28, 24],
    "Salary": [15000, 25000, 18000, 35000, 22000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

# print(df)

#Filtering rows
# result=df[df["Salary"]>20000]
# print(result)

# # Age greater than 23
# result=df[df["Age"] > 23]
# print(result)

# # Employees in IT
# result=df[df["Department"] == "IT"]
# print(result)

# # Salary less than or equal to 22000
# result=df[df["Salary"] <= 22000]
# print(result)

# # Multiple conditions

# # Salary > 20000 AND Age > 23
# r=df[(df["Salary"] > 20000) & (df["Age"] > 23)]
# print(r)    
# # Department is IT OR salary > 30000
# r=df[(df["Department"] == "IT") | (df["Salary"] > 30000)]
# print(r)

#Sorting rows
r=df.sort_values(by="Salary")
# Sort by salary from highest to lowest(descending order)
r=df.sort_values(by="Salary", ascending=False)
print(r)

# Summary statistics for numerical columns
print(df.describe())

# Count occurrences of each department
print(df["Department"].value_counts())