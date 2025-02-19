


# file name : DataCleaningandHandling.py
# Discription : in this file, we will learn Data Cleaning and Handling
# auther : Nasser hadi
# github : https://github.com/3nar




# Data Cleaning & Handling Missing Values in Pandas

'''
Handling missing data is a crucial step in data preprocessing. Pandas provides powerful functions to **detect, fill, and remove missing values**.

---

## **5.1 Checking for Missing Values**
Missing values in Pandas are represented as **NaN (Not a Number)**. You can check for missing values using `isnull()` or `isna()`.

### **5.1.1 Detect Missing Values**
```python
import pandas as pd

# Creating a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 35, 40],  # Missing value in Age
    'City': ['New York', 'Los Angeles', None, 'Chicago'],  # Missing value in City
    'Salary': [50000, 60000, 70000, None]  # Missing value in Salary
}

df = pd.DataFrame(data)

# Check for missing values
print(df.isnull())  # Shows True for missing values
```
#### **Output**
```
    Name    Age   City  Salary
0  False  False  False   False
1  False   True  False   False
2  False  False   True   False
3  False  False  False    True
```

### **5.1.2 Count Missing Values Per Column**
```python
print(df.isnull().sum())  # Counts missing values for each column
```
#### **Output**
```
Name      0
Age       1
City      1
Salary    1
dtype: int64
```

---

## **5.2 Filling Missing Values (`df.fillna()`)**
Instead of removing missing values, we can **fill** them with:
- **A default value (e.g., 0, mean, median, mode, etc.)**
- **Forward fill (`ffill`)**
- **Backward fill (`bfill`)**

### **5.2.1 Fill Missing Values with a Specific Value**
```python
df_filled = df.fillna(0)  # Replace all NaN values with 0
print(df_filled)
```

### **5.2.2 Fill Missing Values with Column Mean (for Numerical Data)**
```python
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Replace missing Age with mean
df['Salary'].fillna(df['Salary'].median(), inplace=True)  # Replace missing Salary with median
```

### **5.2.3 Fill Missing Values with Mode (Most Frequent Value)**
```python
df['City'].fillna(df['City'].mode()[0], inplace=True)  # Replace missing City with mode
```

### **5.2.4 Forward Fill (`ffill`)**
Fills missing values with the previous row’s value.
```python
df.fillna(method='ffill', inplace=True)
```

### **5.2.5 Backward Fill (`bfill`)**
Fills missing values with the next row’s value.
```python
df.fillna(method='bfill', inplace=True)
```

---

## **5.3 Dropping Missing Values (`df.dropna()`)**
If missing values are **significant** and cannot be filled, you may need to **remove** them.

### **5.3.1 Drop Rows with Missing Values**
```python
df_dropped = df.dropna()  # Drops any row that has at least one NaN
print(df_dropped)
```

### **5.3.2 Drop Columns with Missing Values**
```python
df_dropped_cols = df.dropna(axis=1)  # Removes columns that contain NaN
print(df_dropped_cols)
```

### **5.3.3 Drop Rows Only if All Values are Missing**
```python
df.dropna(how='all', inplace=True)
```

### **5.3.4 Drop Rows if a Specific Column has Missing Values**
```python
df.dropna(subset=['Age'], inplace=True)  # Drops rows where 'Age' is NaN
```

---

'''
