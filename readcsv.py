#Read CSV Files
'''
A simple way to store big data sets is to use CSV files (comma separated files).
CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
'''

import pandas as pd

a=pd.read_csv('pandas_practice_employees.csv')
# print(a.to_string())
# print(a)

'''
use to_string() to print the entire DataFrame.
If you have a large DataFrame with many rows, Pandas will only return the first 5 rows(print(a) when we print like this), and the last 5 rows:
'''


# max_rows
'''
The number of rows returned is defined in Pandas option settings.
You can check your system's maximum rows with the pd.options.display.max_rows statement.
'''
print(pd.options.display.max_rows) 
#60
'''
In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
You can change the maximum rows number with the same statement.
'''
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df) 