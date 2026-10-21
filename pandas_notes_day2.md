# Pandas Notes --- Day 2

These notes cover the Pandas data-cleaning topics learned today. Your
original code and comments are included, with simple explanations and
examples added for revision.

## 1. Handling Empty Cells

Empty or missing cells can cause incorrect results during data analysis.
Pandas commonly represents missing values as `NaN`.

### Removing rows with missing values: `dropna()`

`dropna()` returns a new DataFrame with rows containing missing values
removed. By default, the original DataFrame is not changed.

``` python
#Empty Cells
'''
Empty cells can potentially give you a wrong result when you analyze data.
'''

#Remove Rows
'''
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
'''

import pandas as pd
df=pd.read_csv("messdata.csv")
# print(df.columns)
# new_df=df.dropna()
# print(new_df.to_string())
# print(df.isna().sum()) # counts the missing values in each column.

'''Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
If you want to change the original DataFrame, use the inplace = True argument:
'''
# df.dropna(inplace = True)
```

Useful points: - `df.isna().sum()` counts missing values in each
column. - `new_df = df.dropna()` saves the cleaned DataFrame in
`new_df`. - `df.dropna(inplace=True)` changes `df` directly.

### Replacing missing values: `fillna()`

`fillna()` fills missing cells with a value you provide.

``` python
#Replace Empty Values
'''
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:
'''

# c=df.fillna("hell no")
# print(c.to_string())
```

Example:

``` python
new_df = df.fillna(0)
```

This replaces missing values throughout the DataFrame with `0`. Unless
you assign the result or use `inplace=True` where supported, the
original DataFrame remains unchanged.

### Replacing values in a specific column

``` python
#Replace Only For Specified Columns
'''
The example above replaces all empty cells in the whole Data Frame.
To only replace empty values for one column, specify the column name for the DataFrame:
'''
# a=df.fillna({"Calories": "hello"})
# print(a.c ())
```

Example:

``` python
new_df = df.fillna({"Calories": 0})
```

This fills missing values only in the `Calories` column. Using a text
value such as `"hello"` also works, but it can make a numeric column
unsuitable for calculations.

### Filling missing values with the mode

The **mode** is the most frequent value in a column. `mode()` returns a
Series, which can contain more than one value if there is a tie.

``` python
#Replace Using Mean, Median, or Mode

x=df["Calories"].mode()
a=df.fillna({"Calories":x})
print(a)
```

If you want to use one mode value to fill every missing cell, select a
single value from the Series:

``` python
x = df["Calories"].mode()[0]
a = df.fillna({"Calories": x})
print(a)
```

Why `[0]` matters: - `mode()` returns a Series. - `mode()[0]` selects
the first mode value as a scalar. - `fillna()` with a scalar uses the
same value for every missing cell in that column. - Passing a Series to
`fillna()` aligns its index with the DataFrame's index, so it may fill
only matching index positions.

## 2. Cleaning Data with the Wrong Format

Cells with inconsistent formats can make analysis difficult. For
example, dates may be stored in different formats or as text.

### Converting values to datetime

`pd.to_datetime()` converts a column to datetime values. The
`format="mixed"` option lets Pandas infer formats for individual values
when date formats differ.

``` python
#Pandas - Cleaning Data of Wrong Format

'''
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
'''

import pandas as pd
df=pd.read_csv("messdata.csv")
df['Date']=pd.to_datetime(df['Date'], format="mixed")
print(df.to_string())
```

### Handling missing dates with `NaT`

`NaT` means **Not a Time**. It is the datetime equivalent of a missing
value, and can be handled with `dropna()`.

``` python
'''
As you can see from the result, the date in row 26 was fixed, but the empty date got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.
'''

# Removing Rows
'''
The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
'''
a=df.dropna(subset=['Date'])
print(a.to_string())
```

`subset=['Date']` tells `dropna()` to remove only rows where the `Date`
column is missing. Missing values in other columns do not by themselves
cause a row to be removed by this call.

## 3. Fixing Wrong Data

Wrong data is data that is present but incorrect, such as a typo or an
impossible value. You should use knowledge of the dataset to decide what
counts as wrong.

### Replacing a specific value

Use `.loc[row_index, "column"]` to update a particular cell.

``` python
#Pandas - Fixing Wrong Data
'''
"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
'''

# Replacing Values
'''
One way to fix wrong values is to replace them with something else.
In our example, it is most likely a typo, and the value should be "60" instead of "160", and we could just insert "60" in row 31:
'''
import pandas as pd
df=pd.read_csv("messdata.csv")
# df.loc[31, 'Duration'] = 45
# print(df.to_string())
```

Example:

``` python
df.loc[31, "Duration"] = 60
```

This changes the `Duration` value at index `31` to `60`. Check the row
index and the intended correction before changing real data.

### Correcting values using a rule

For larger datasets, you can define a rule to find values outside an
expected range. The correct replacement depends on the data; don't
change values automatically without checking what is reasonable.

``` python
'''
For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
'''
# for x in df.index:
#     if df.loc[x,"Duration"]>120:
#         df.loc[x,"Duration"]=120
# print(df.to_string())
```

### Removing rows containing wrong data

You can remove rows that contain values considered invalid for your
analysis.

``` python
# Removing Rows
'''
Another way of handling wrong data is to remove the rows that contains wrong data.
This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
'''

for x in df.index:
  if df.loc[x, "Duration"] > 120:
        df=df.drop(x)
print(df.to_string())
```

A shorter alternative is filtering:

``` python
df = df[df["Duration"] <= 120]
```

This keeps rows where `Duration` is `120` or less. The threshold should
make sense for the dataset.

## 4. Removing Duplicates

Duplicate rows are rows repeated more than once. `duplicated()` returns
a Boolean Series indicating whether each row is a duplicate of an
earlier row. The first occurrence is marked `False`; repeated
occurrences are marked `True`.

``` python
#Pandas - Removing Duplicates
'''
Duplicate rows are rows that have been registered more than one time.
To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row:
'''
import pandas as pd
df=pd.read_csv("messdata.csv")
print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df.to_string())
```

-   `df.duplicated()` identifies duplicate rows; it does not remove
    them.
-   `df.drop_duplicates()` returns a DataFrame with duplicate rows
    removed.
-   `inplace=True` changes `df` directly.

## Quick Revision

  ----------------------------------------------------------------------------------
  Method / expression                            Purpose
  ---------------------------------------------- -----------------------------------
  `df.isna().sum()`                              Count missing values in each column

  `df.dropna()`                                  Return rows without missing values

  `df.dropna(inplace=True)`                      Remove rows with missing values
                                                 from the original DataFrame

  `df.fillna(value)`                             Replace missing values with a
                                                 specified value

  `df.fillna({"Calories": 0})`                   Fill missing values in one
                                                 specified column

  `df["Calories"].mode()`                        Return the most frequent value(s)
                                                 as a Series

  `df["Calories"].mode()[0]`                     Select the first mode value

  `pd.to_datetime(df["Date"], format="mixed")`   Convert date values to datetime

  `df.dropna(subset=["Date"])`                   Remove rows with missing dates

  `df.loc[index, "Duration"] = value`            Replace a particular cell's value

  `df = df[df["Duration"] <= 120]`               Keep rows that meet a condition

  `df.duplicated()`                              Identify duplicate rows

  `df.drop_duplicates(inplace=True)`             Remove duplicate rows in place
  ----------------------------------------------------------------------------------
