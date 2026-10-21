# Pandas Notes

These notes collect the Pandas topics learned so far, in learning order.
Existing code examples and comments are preserved, with short
explanations added where useful.

## 1. Pandas Basics

### Checking the Pandas version

Use `pd.__version__` to check which Pandas version is installed.

``` python
import pandas as pd
print(pd.__version__)
```

### Reading a CSV file

``` python
#example
# import pandas as pd

# df=pd.read_csv("pandas_practice_employees.csv")

# print(df.to_string())
```

### Creating a DataFrame

A Pandas **DataFrame** is a two-dimensional, table-like structure with
rows and columns, similar to an Excel spreadsheet.

``` python
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
```

**Remember:** - `pd.DataFrame(data)` creates a DataFrame from data such
as a dictionary. - `a["passings"]` selects one column and returns a
**Series**. - `a[["passings"]]` selects one column but keeps the result
as a **DataFrame**.

## 2. Pandas Series

A Pandas **Series** is a one-dimensional structure that holds values,
similar to one column of a table.

### Creating a Series from a list

``` python
import pandas as pd
# A Pandas Series is like a column in a table.
'''
It is a one-dimensional array holding data of any type.
'''

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
```

If you do not specify labels, Pandas uses index labels starting from
`0`.

### Creating a Series from a dictionary value

``` python
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

b = pd.Series(mydataset["cars"])
print(b)

#pd.Series(mydataset["cars"]) → explicitly creates a Series.
#a["cars"] → selects the column as a Series.
```

Both can produce a Series, but they work differently: - `pd.Series(...)`
creates a Series. - `a["cars"]` selects a column from an existing
DataFrame named `a`.

### Labels and accessing values

The default labels are index numbers. You can use a label to access its
corresponding value.

``` python
# Labels
'''
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
'''
print(myvar[0])
```

### Creating custom labels

Use the `index` argument to set your own labels.

``` python
# Create Labels
'''
With the index argument, you can name your own labels.
'''

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])
```

### Creating a Series from a dictionary

Dictionary keys become the Series labels, and dictionary values become
the data.

``` python
#Key/Value Objects as Series
'''
You can also use a key/value object, like a dictionary, when creating a Series.
'''
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
```

### Selecting specific dictionary items

Use the `index` argument to include only selected dictionary keys.

``` python
'''
To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
'''

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)
```

## 3. Pandas DataFrames

A Pandas DataFrame is a **two-dimensional** data structure, like a table
with rows and columns.

### Creating a DataFrame

``` python
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
```

### Locating rows with `loc`

Use `loc` to access rows by their index label. With the default index,
those labels are `0`, `1`, `2`, and so on.

``` python
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
```

-   `b.loc[1]` returns one row as a Series.
-   `b.loc[[0, 1]]` returns multiple rows as a DataFrame.

### Named indexes

You can provide custom index labels when creating a DataFrame.

``` python
#Named Indexes
c=pd.DataFrame(a,index=["player1","player2","player3"])
print(c)
#Locate Named Indexes
print(c.loc["player1"])
```

### Loading a CSV file into a DataFrame

``` python
#Load Files Into a DataFrame
'''
If your data sets are stored in a file, Pandas can load them into a DataFrame.
Example
Load a comma separated file (CSV file) into a DataFrame:
'''
df = pd.read_csv('pandas_practice_employees.csv')

print(df)
```

## 4. Reading CSV and JSON Files

### Reading CSV files

CSV means **comma-separated values**. It is a common plain-text format
for storing tabular data.

``` python
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
```

-   `pd.read_csv("file.csv")` loads a CSV file into a DataFrame.
-   `print(a)` displays a shortened view when the DataFrame is large.
-   `print(a.to_string())` displays the entire DataFrame.

### Understanding `display.max_rows`

Pandas has display options that control how many rows it shows when
printing a DataFrame.

``` python
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
# pd.options.display.max_rows = 9999
# df = pd.read_csv('data.csv')
# print(df) 
```

The value `60` is the setting shown in the original example; it can
differ by environment. You can change it with
`pd.options.display.max_rows = 9999`.

### Reading JSON files

JSON is another common text format for storing or exchanging data. Use
`pd.read_json()` to load a JSON file.

``` python
# Read JSON
'''
Big data sets are often stored, or extracted as JSON.
JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
'''

df = pd.read_json('data.json')
print(df.to_string())
```

## 5. Viewing Data

### Viewing the first rows with `head()`

The `head()` method shows the first rows of a DataFrame. By default, it
displays the first five rows. You can provide a number to choose how
many rows to show.

``` python
# Viewing the Data
'''
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.
'''

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

'''
if the number of rows is not specified, the head() method will return the top 5 rows.

'''
df = pd.read_csv('data.csv')

print(df.head())
```

### Viewing the last rows with `tail()`

The `tail()` method shows rows from the bottom of the DataFrame. By
default, it displays the last five rows.

``` python
'''
There is also a tail() method for viewing the last rows of the DataFrame.
The tail() method returns the headers and a specified number of rows, starting from the bottom.
'''

print(df.tail()) 
```

### Getting information with `info()`

The `info()` method provides a quick summary of the DataFrame, including
column names, non-null counts, data types, and memory usage.

``` python
# Info About the Data
'''
The DataFrames object has a method called info(), that gives you more information about the data set.
'''
print(df.info()) 
```

## Quick Revision

  -----------------------------------------------------------------------
  Concept                             Purpose
  ----------------------------------- -----------------------------------
  `pd.__version__`                    Check the installed Pandas version

  `pd.Series(data)`                   Create a one-dimensional Series

  `pd.DataFrame(data)`                Create a two-dimensional table

  `df["column"]`                      Select one column as a Series

  `df[["column"]]`                    Select one column as a DataFrame

  `df.loc[label]`                     Select a row by its index label

  `pd.read_csv("file.csv")`           Read a CSV file

  `pd.read_json("file.json")`         Read a JSON file

  `df.to_string()`                    Display the complete DataFrame

  `df.head()`                         View the first five rows by default

  `df.tail()`                         View the last five rows by default

  `df.info()`                         Get a summary of the DataFrame

  `pd.options.display.max_rows`       Check or change the row-display limit

  
  -----------------------------------------------------------------------
