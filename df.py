'''What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
'''

import pandas as pd

a={
    'players':["Messi","Ronaldo","Neymar"],
    'stats':[93,92,90]
}
b=pd.DataFrame(a)
# print(b)

# Locate Row
'''
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
df.loc[row_label, column_label]
'''

# print(b.loc[1])
#Note: This example returns a Pandas Series.

#use a list of indexes:
# print(b.loc[[0, 1]])
#Note: When using [], the result is a Pandas DataFrame

#Named Indexes
# c=pd.DataFrame(a,index=["player1","player2","player3"])
# print(c)
# #Locate Named Indexes
# print(c.loc["player1"])


#Load Files Into a DataFrame
'''
If your data sets are stored in a file, Pandas can load them into a DataFrame.
Example
Load a comma separated file (CSV file) into a DataFrame:
'''
df = pd.read_csv('pandas_practice_employees.csv')

# print(df) 

# iloc[] — select using integer positions

'''
df.iloc[row_position, column_position]
Here, positions start at 0, just like Python lists.
'''


data = {
    "Name": ["Arun", "Rahul", "Priya", "Anu"],
    "Age": [22, 25, 23, 24],
    "Salary": [20000, 30000, 25000, 28000],
    "Department": ["IT", "HR", "IT", "Sales"]
}

df = pd.DataFrame(data)
print(df)

print(df.iloc[1])

# Select one specific value
print(df.iloc[1, 0])

#Select the first three rows
print(df.iloc[0:3])

#Select rows and columns by position
print(df.iloc[0:3, 0:2])


'''
loc[] vs iloc[]
Feature	                loc[]	                iloc[]
Uses	                Index/column labels	    Integer positions
Select a value	        df.loc[1, "Name"]	    df.iloc[1, 0]
End of a slice	        Included	            Excluded
Select all rows	        df.loc[:, "Name"]	    df.iloc[:, 0]

Easy way to remember: loc = label, iloc = integer position.
'''