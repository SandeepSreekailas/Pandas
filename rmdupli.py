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