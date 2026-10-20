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

