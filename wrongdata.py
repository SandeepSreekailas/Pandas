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

'''
For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
'''
# for x in df.index:
#     if df.loc[x,"Duration"]>120:
#         df.loc[x,"Duration"]=120
# print(df.to_string())

# Removing Rows
'''
Another way of handling wrong data is to remove the rows that contains wrong data.
This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
'''

for x in df.index:
  if df.loc[x, "Duration"] > 120:
        df=df.drop(x)
print(df.to_string())
    

