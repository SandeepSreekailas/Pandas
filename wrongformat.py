#Pandas - Cleaning Data of Wrong Format

'''
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
'''

import pandas as pd
df=pd.read_csv("messdata.csv")
df['Date']=pd.to_datetime(df['Date'], format="mixed")
print(df.to_string())

'''
As you can see from the result, the date in row 26 was fixed, but the empty date got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.
'''

# Removing Rows
'''
The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
'''
a=df.dropna(subset=['Date'])
print(a.to_string())