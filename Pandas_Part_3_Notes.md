# Pandas Notes --- Part 3

Topics: correlation, plotting, filtering, sorting, statistics, grouping,
merging, concatenation, data types, dates, and missing values.

## 1. Correlation (`corr()`)

Correlation measures the strength and direction of a **linear
relationship** between numerical columns.

``` python
df.corr(numeric_only=True)
```

  Value       Meaning
  ----------- ------------------------------
  `+1`        Perfect positive correlation
  Near `+1`   Strong positive relationship
  `0`         No linear relationship
  Near `-1`   Strong negative relationship
  `-1`        Perfect negative correlation

Example:

``` python
df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
})
df.corr(numeric_only=True)
```

**Remember:** Correlation does not prove causation. Zero correlation
does not rule out a nonlinear relationship.

## 2. Plotting

``` python
df.plot(x="Date", y="Sales", kind="line")       # Trends
df.plot(x="Product", y="Sales", kind="bar")     # Compare categories
df["Age"].plot(kind="hist")                     # Distribution
df.plot(x="Hours", y="Marks", kind="scatter")   # Relationship
```

  Plot        Purpose
  ----------- ----------------------------------------------
  `line`      Trends over time or ordered values
  `bar`       Compare categories
  `hist`      Numerical data distribution
  `scatter`   Relationship between two numerical variables

## 3. Filtering Data

Filtering selects rows that satisfy a condition.

``` python
data = {
    "Name": ["Arun", "Binu", "Charan", "Deepa", "Eva"],
    "Age": [22, 25, 21, 28, 24],
    "Salary": [15000, 25000, 18000, 35000, 22000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}
df = pd.DataFrame(data)
```

### Single condition

``` python
df[df["Salary"] > 20000]
df[df["Age"] >= 25]
df[df["Department"] == "IT"]
df[df["Salary"] <= 22000]
```

### Multiple conditions

``` python
df[(df["Salary"] > 20000) & (df["Age"] > 23)]  # AND: both true
df[(df["Department"] == "IT") | (df["Salary"] > 30000)]  # OR: either true
```

Use parentheses around each condition.

-   `==` equal to; `!=` not equal to
-   `>` greater than; `<` less than
-   `>=` greater than or equal to; `<=` less than or equal to
-   `&` AND; `|` OR

## 4. Sorting (`sort_values()`)

``` python
df.sort_values(by="Salary")  # Ascending: lowest first
df.sort_values(by="Salary", ascending=False)  # Descending: highest first
df.sort_values(by=["Department", "Salary"])  # Sort by multiple columns
```

Store the result:

``` python
result = df.sort_values(by="Salary", ascending=False)
```

This creates a new DataFrame and does not change `df`. To modify the
original DataFrame, you can use `inplace=True`:

``` python
df.sort_values(by="Salary", ascending=False, inplace=True)
```

## 5. Descriptive Statistics (`describe()`)

``` python
df.describe()
```

  Statistic   Meaning
  ----------- ------------------------------
  `count`     Number of non-missing values
  `mean`      Average
  `std`       Standard deviation
  `min`       Minimum
  `25%`       First quartile
  `50%`       Median
  `75%`       Third quartile
  `max`       Maximum

Individual calculations:

``` python
df["Salary"].mean()
df["Salary"].max()
df["Salary"].min()
df["Salary"].sum()
df["Salary"].count()
```

## 6. Counting Values (`value_counts()`)

Counts how often each unique value occurs in a Series.

``` python
df["Department"].value_counts()
df["Department"].value_counts(ascending=True)
```

Example result:

``` text
HR         2
IT         2
Finance    1
```

`value_counts()` is a quick way to count unique values. `groupby()` is
more flexible for calculations.

``` python
df["Department"].value_counts()
df.groupby("Department").size()
```

## 7. Grouping and Aggregation (`groupby()`)

Group rows by a column, then calculate statistics.

``` python
df.groupby("Department")["Salary"].mean()  # Average salary
df.groupby("Department")["Salary"].sum()   # Total salary
df.groupby("Department")["Salary"].max()   # Highest salary
df.groupby("Department").size()             # Number of rows per group
```

Multiple calculations:

``` python
df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum"])
```

Aggregate multiple columns:

``` python
df.groupby("Department").agg({
    "Salary": ["mean", "max"],
    "Name": "count"
})
```

-   `size()` counts rows, even if other columns contain missing values.
-   `count()` counts non-missing values in the selected column.
-   `agg()` applies one or more aggregation functions.

## 8. Combining DataFrames: `merge()` and `concat()`

### `merge()`

Combines DataFrames using a common column/key, similar to a SQL JOIN.

``` python
employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Arun", "Binu", "Charan"]
})
salaries = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Salary": [15000, 25000, 18000]
})

result = pd.merge(employees, salaries, on="EmpID")
```

`on="EmpID"` specifies the common key.

``` python
pd.merge(employees, salaries, on="EmpID", how="inner")
pd.merge(employees, salaries, on="EmpID", how="left")
pd.merge(employees, salaries, on="EmpID", how="right")
pd.merge(employees, salaries, on="EmpID", how="outer")
```

  `how`     Meaning
  --------- ----------------------------------------
  `inner`   Only matching keys
  `left`    All left rows plus matching right rows
  `right`   All right rows plus matching left rows
  `outer`   All keys from both DataFrames

Default: `how="inner"`.

### `concat()`

Combines DataFrames by stacking rows or placing columns side by side.

``` python
pd.concat([df1, df2], axis=0, ignore_index=True)  # Stack rows
pd.concat([df1, df2], axis=1)                     # Place columns side by side
```

  Axis       In `concat()`          In `sum()`
  ---------- ---------------------- ---------------------------------
  `axis=0`   Stack vertically       Sum each column
  `axis=1`   Combine horizontally   Sum across columns for each row

`concat(axis=1)` aligns rows by index. Missing columns or unmatched
indexes can result in `NaN`.

**Difference:** Use `merge()` to combine data based on matching keys.
Use `concat()` to stack or join DataFrames along rows or columns.

## 9. Checking and Handling Data Types

Each DataFrame column has a data type (`dtype`).

``` python
df.dtypes           # Data types of all columns
df["Salary"].dtype  # Data type of one column
```

  Type               Common use
  ------------------ ---------------------------------------
  `int64`            Integers
  `float64`          Decimal numbers
  `object`           Often strings or mixed Python objects
  `bool`             `True` / `False`
  `datetime64[ns]`   Dates and times
  `string`           Pandas' dedicated text type

### Convert types with `astype()`

``` python
df["Age"] = df["Age"].astype(int)
df["Age"] = df["Age"].astype(float)
df["Name"] = df["Name"].astype("string")
```

Example with an age column stored as strings:

``` python
df = pd.DataFrame({
    "Name": ["Arun", "Binu", "Charan"],
    "Age": ["22", "25", "21"]
})
df["Age"] = df["Age"].astype(int)
```

`astype(int)` raises an error if values contain invalid text, such as
`"unknown"`.

### Python list vs Pandas Series

``` python
names = ["Arun", "Binu", "Charan"]

type(names)       # list
type(names[0])    # str

df = pd.DataFrame({"Name": names})
type(df["Name"])     # pandas Series
type(df["Name"][0])  # str
df["Name"].dtype     # usually object
```

The input is a Python list, but the DataFrame column is a Pandas Series.
Each cell still contains a Python string.

## 10. Working with Dates (`to_datetime()`)

Dates may initially be stored as strings. Convert them to datetime
format for date-based operations.

``` python
df = pd.DataFrame({
    "Name": ["Arun", "Binu", "Charan"],
    "Joining_Date": ["2024-01-10", "2023-06-15", "2025-03-20"]
})
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
```

Extract date components using `.dt`:

``` python
df["Year"] = df["Joining_Date"].dt.year
df["Month"] = df["Joining_Date"].dt.month
df["Day"] = df["Joining_Date"].dt.day
df["Day_Name"] = df["Joining_Date"].dt.day_name()
```

Handle invalid dates:

``` python
df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    errors="coerce"
)
```

With `errors="coerce"`, invalid dates become `NaT` (Not a Time).

Filter by date:

``` python
df[df["Joining_Date"] >= "2024-01-01"]
```

## 11. Missing Values (`isna()`, `notna()`, `dropna()`, `fillna()`)

### Check missing values

``` python
df.isna()             # True where values are missing
df["Name"].isna()     # Check one column
df.isna().sum()       # Count missing values per column
df.notna()            # True where values are not missing
```

`isna()` is a function name, not an officially defined acronym with a
full form.

### Remove missing values

``` python
df.dropna()  # Remove rows containing missing values
df.dropna(subset=["Joining_Date"])  # Remove rows missing this date
```

### Fill missing values

``` python
df["Age"] = df["Age"].fillna(0)
df["Name"] = df["Name"].fillna("Unknown")
```

-   `isna()` --- identify missing values.
-   `notna()` --- identify non-missing values.
-   `dropna()` --- remove missing data.
-   `fillna()` --- replace missing data.

## Quick Revision Sheet

  Topic                     Main methods
  ------------------------- ---------------------------------------------------
  Correlation               `corr()`
  Plotting                  `plot()`
  Filtering                 `df[condition]`
  Sorting                   `sort_values()`
  Statistics                `describe()`, `mean()`, `sum()`, `min()`, `max()`
  Counting unique values    `value_counts()`
  Grouping                  `groupby()`, `agg()`
  Combine by key            `merge()`
  Combine by rows/columns   `concat()`
  Check data types          `dtypes`, `dtype`
  Convert data types        `astype()`
  Convert dates             `to_datetime()`
  Extract date components   `.dt.year`, `.dt.month`, `.dt.day`
  Missing values            `isna()`, `notna()`, `dropna()`, `fillna()`

