import pandas as pd
# A Pandas Series is like a column in a table.
'''
It is a one-dimensional array holding data of any type.
'''

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

b = pd.Series(mydataset["cars"])
print(b)

#pd.Series(mydataset["cars"]) → explicitly creates a Series.
#a["cars"] → selects the column as a Series.


# Labels
'''
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
'''
print(myvar[0])

# Create Labels
'''
With the index argument, you can name your own labels.
'''

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])

#Key/Value Objects as Series
'''
You can also use a key/value object, like a dictionary, when creating a Series.
'''
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

'''
To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
'''

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)