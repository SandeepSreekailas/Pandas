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


#Replace Empty Values
'''
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:
'''

# c=df.fillna("hell no")
# print(c.to_string())

#Replace Only For Specified Columns
'''
The example above replaces all empty cells in the whole Data Frame.
To only replace empty values for one column, specify the column name for the DataFrame:
'''
# a=df.fillna({"Calories": "hello"})
# print(a.c ())

#Replace Using Mean, Median, or Mode

x=df["Calories"].mode()
a=df.fillna({"Calories":x})
print(a)