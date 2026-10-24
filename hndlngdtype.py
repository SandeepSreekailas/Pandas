# Handling data types and dates 
'''
This topic is useful because CSV files often contain numbers stored as text, or dates that Pandas doesn't automatically recognize as dates.
'''

import pandas as pd

df = pd.DataFrame({
    "Name": ["Arun", "Binu", "Charan"],
    "Age": ["22", "25", "21"],
    "Salary": [15000, 25000, 18000],
    "Joining_Date": ["2024-01-10", "2023-06-15", "2025-03-20"]
})

# print(df.dtypes)

# df["Age"]=df["Age"].astype(int)
# print(df.dtypes)
# df["Age"] = df["Age"].astype(float)
# print(df.dtypes)
# df["Name"] = df["Name"].astype(str)
# print(df.dtypes)
# print(type(df["Name"][0]))
'''
Use astype() when you know the existing values can be converted to the requested type.
'''

# Convert strings into dates
df["Joining_Date"]=pd.to_datetime(df["Joining_Date"])
print(df.dtypes)

#Extract year, month and day
# df["Year"]=df["Joining_Date"].dt.year
# df["Month"]=df["Joining_Date"].dt.month
# df["Day"]=df["Joining_Date"].dt.day
# print(df)
# Employees who joined after 1 January 2024
# a=df[df["Joining_Date"] > "2024-03-01"]
# print(a)

#You can also extract the day of the week:
# df["Weekday"] = df["Joining_Date"].dt.day_name()
# print(df)

#What if some dates are invalid?
df = pd.DataFrame({
    "Date": ["2024-01-10", "not-a-date", "2025-03-20"]
})

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
print(df)

'''
errors="coerce" converts invalid dates into NaT (Not a Time), instead of raising an error.
You can then find missing dates:
'''
a=df["Date"].isna()
print(a)
'''
Or you can remove them:
'''
df.dropna(subset=["Date"], inplace=True)
print(df)
'''
Method	Purpose
df.dtypes	Check column data types
.astype(int)	Convert to integer
.astype(float)	Convert to decimal numbers
pd.to_datetime()	Convert values to dates
errors="coerce"	Invalid conversions become missing values
.dt.year	Extract year
.dt.month	Extract month
.dt.day	Extract day
dropna(subset=["Date"])	Remove rows with missing dates
'''

'''
Method	Meaning
df.isna()	Check for missing values
df.notna()	Check for non-missing values
df.isna().sum()	Count missing values
df.dropna()	Remove rows with missing values
'''