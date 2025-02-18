


# file name : SelectingandIndexingDatainPandas.py
# Discription : in this file, we will learn Selecting and Indexing Data in Pandas.py
# auther : Nasser hadi
# github : https://github.com/3nar




# Selecting & Indexing Data in Pandas

'''
Selecting and indexing data is one of the most **important** operations in Pandas. You will frequently need to extract specific **columns, rows, or subsets of data**.

---

## **4.1 Selecting Columns**
### **4.1.1 Selecting a Single Column**
To select a single column from a **DataFrame**, use **square brackets** `[]`:
```python
import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Selecting a single column
print(df['Name'])
```
#### **Output**
```
0    Alice
1      Bob
2  Charlie
Name: Name, dtype: object
```
- This returns a **Series**.

---

### **4.1.2 Selecting Multiple Columns**
To select multiple columns, pass a **list of column names**:
```python
df_subset = df[['Name', 'Age']]
print(df_subset)
```
#### **Output**
```
     Name  Age
0   Alice   25
1     Bob   30
2  Charlie   35
```
- This returns a **DataFrame**.

---

## **4.2 Selecting Rows**
### **4.2.1 Selecting Rows by Index using `.loc[]`**
`.loc[]` is used for **label-based indexing** (using row labels).
```python
# Select row where index = 1
print(df.loc[1])
```
#### **Output**
```
Name         Bob
Age           30
City    Los Angeles
Name: 1, dtype: object
```
- Returns a **Series** representing the row.

---

### **4.2.2 Selecting Rows by Position using `.iloc[]`**
`.iloc[]` is used for **position-based indexing** (like Python lists).
```python
# Select the second row (index 1)
print(df.iloc[1])
```
#### **Output (Same as Above)**
```
Name         Bob
Age           30
City    Los Angeles
Name: 1, dtype: object
```
---

### **4.2.3 Selecting Multiple Rows**
Use a **list of indexes** to get multiple rows:
```python
print(df.loc[[0, 2]])  # Select rows at index 0 and 2
```
or use slicing with `.iloc[]`:
```python
print(df.iloc[0:2])  # Select the first two rows
```
#### **Output**
```
     Name  Age      City
0   Alice   25  New York
1     Bob   30  Los Angeles
```

---

## **4.3 Boolean Indexing (Filtering Data)**
Boolean indexing allows you to filter data based on conditions.

### **4.3.1 Filtering Rows Based on a Condition**
```python
# Select rows where Age > 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)
```
#### **Output**
```
     Name  Age     City
2  Charlie   35  Chicago
```
---

### **4.3.2 Filtering with Multiple Conditions**
Use **& (AND)** and **| (OR)** for multiple conditions.

#### **Filter where Age > 25 AND City is 'New York'**
```python
df_filtered = df[(df['Age'] > 25) & (df['City'] == 'New York')]
print(df_filtered)
```

#### **Filter where Age > 30 OR City is 'Los Angeles'**
```python
df_filtered = df[(df['Age'] > 30) | (df['City'] == 'Los Angeles')]
print(df_filtered)
```

---

## **4.4 Selecting Specific Rows & Columns Together**
### **Select a Specific Row & Column**
```python
print(df.loc[1, 'Name'])  # Get the Name of row at index 1
```
#### **Output**
```
Bob
```

### **Select Multiple Rows & Columns**
```python
print(df.loc[[0, 2], ['Name', 'City']])  # Select specific rows & columns
```
#### **Output**
```
     Name      City
0   Alice  New York
2  Charlie   Chicago
```

---

'''
