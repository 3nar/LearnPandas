


# file name : PandasDataStructures.py
# Discription : in this file, we will learn Pandas with Data Structures
# auther : Nasser hadi
# github : https://github.com/3nar




# Pandas Data Structures

'''
Pandas provides two primary data structures:

1. **Series** → One-dimensional labeled array (like a column in Excel)  
2. **DataFrame** → Two-dimensional table (like an entire spreadsheet)  

---

## **2.1 Series (1D Array)**  
A **Series** is a one-dimensional array that stores **data + labels (index)**.

### **2.1.1 Creating a Pandas Series**
First, ensure you have Pandas imported:
```python
import pandas as pd
```

Now, create a simple Series from a **Python list**:
```python
data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)
```

#### **Output**
```
0    10
1    20
2    30
3    40
dtype: int64
```
- The **left column** is the **index** (default is 0,1,2,...).
- The **right column** contains the **values**.

---

### **2.1.2 Creating a Series with a Custom Index**
You can specify custom labels (instead of default 0,1,2,...).
```python
data = [100, 200, 300, 400]
index_labels = ['a', 'b', 'c', 'd']

series = pd.Series(data, index=index_labels)
print(series)
```
#### **Output**
```
a    100
b    200
c    300
d    400
dtype: int64
```
Now, we can access values using these **custom labels**:
```python
print(series['b'])  # Output: 200
```

---

### **2.1.3 Creating a Series from a Dictionary**
A **dictionary** can be directly converted into a Series:
```python
data_dict = {'Alice': 90, 'Bob': 85, 'Charlie': 95}
series = pd.Series(data_dict)
print(series)
```
#### **Output**
```
Alice      90
Bob        85
Charlie    95
dtype: int64
```

---

## **2.2 DataFrame (2D Table)**
A **DataFrame** is a 2D table similar to an **Excel spreadsheet** or a **SQL table**.

### **2.2.1 Creating a DataFrame from a Dictionary**
```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
```
#### **Output**
```
     Name  Age         City
0   Alice   25     New York
1     Bob   30  Los Angeles
2  Charlie   35     Chicago
```
Each **column** in a DataFrame is a **Series**.

---

### **2.2.2 Checking Data in a DataFrame**
Once you have a DataFrame, you should check its structure:

#### **View the First Few Rows (`head()`)**
```python
print(df.head())  # Default: first 5 rows
```

#### **View the Last Few Rows (`tail()`)**
```python
print(df.tail())  # Default: last 5 rows
```

#### **Get a Summary of the Data (`info()`)**
```python
print(df.info())
```
This shows:
- Number of rows and columns
- Data types of each column
- Memory usage

#### **Get Basic Statistics (`describe()`)**
```python
print(df.describe())
```
This gives summary statistics (only for numerical columns):
```
             Age
count   3.000000
mean   30.000000
std     5.000000
min    25.000000
25%    27.500000
50%    30.000000
75%    32.500000
max    35.000000
```

---

''' 
