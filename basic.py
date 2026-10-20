#example
# import pandas as pd

# df=pd.read_csv("pandas_practice_employees.csv")

# print(df.to_string())



#basics
#Checking Pandas Version
import pandas as pd
print(pd.__version__)

#Pandas Getting Started
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
#pd.DataFrame() converts data into a table-like structure with rows and columns, similar to an Excel spreadsheet.
a=pd.DataFrame(mydataset)
print(a)
print(a["passings"])

# print(type(a["passings"]))
# pandas.core.series.Series

# print(type(a[["passings"]]))
# pandas.core.frame.DataFrame

'''
- "passings" is a string representing one column name.
- ["passings"] is a list containing a column name.
Pandas interprets these two selections differently.
'''
