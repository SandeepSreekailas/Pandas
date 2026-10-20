'''What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
'''

import pandas as pd

a={
    'players':["Messi","Ronaldo","Neymar"],
    'stats':[93,92,90]
}
b=pd.DataFrame(a)
print(b)

# Locate Row
'''
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
'''

print(b.loc[1])
#Note: This example returns a Pandas Series.

#use a list of indexes:
print(b.loc[[0, 1]])
#Note: When using [], the result is a Pandas DataFrame

#Named Indexes
c=pd.DataFrame(a,index=["player1","player2","player3"])
print(c)
#Locate Named Indexes
print(c.loc["player1"])


#Load Files Into a DataFrame
'''
If your data sets are stored in a file, Pandas can load them into a DataFrame.
Example
Load a comma separated file (CSV file) into a DataFrame:
'''
df = pd.read_csv('data.csv')

print(df) 