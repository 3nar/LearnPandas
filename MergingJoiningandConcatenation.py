


# file name : MergingJoiningandConcatenation.py
# Discription : in this file, we will learn Merging Joining and Concatenation
# auther : Nasser hadi
# github : https://github.com/3nar




# Merging, Joining, and Concatenation in Pandas

'''
Pandas provides powerful functions to **combine multiple datasets** efficiently. Let's explore:  
✅ **Concatenation (`pd.concat()`)** → Stacking DataFrames **vertically/horizontally**  
✅ **Merging (`pd.merge()`)** → SQL-like **joins** (inner, left, right, outer)  
✅ **Joining (`df.join()`)** → Index-based merging  

---

## **7.1 Concatenation (`pd.concat()`)**  
Concatenation is used to **stack multiple DataFrames** either:  
✔ **Vertically (row-wise)** → `axis=0` (default)  
✔ **Horizontally (column-wise)** → `axis=1`  

### **7.1.1 Vertical Concatenation (Adding Rows)**
```python
import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Concatenating row-wise
df_concat = pd.concat([df1, df2], ignore_index=True)
print(df_concat)
```
#### **Output**
```
   A  B
0  1  3
1  2  4
2  5  7
3  6  8
```
- `ignore_index=True` resets the index after concatenation.

---

### **7.1.2 Horizontal Concatenation (Adding Columns)**
```python
df_concat_col = pd.concat([df1, df2], axis=1)
print(df_concat_col)
```
#### **Output**
```
   A  B  A  B
0  1  3  5  7
1  2  4  6  8
```
- This joins the DataFrames **side by side**.

---

## **7.2 Merging DataFrames (`pd.merge()`)**  
Merging works **like SQL joins** to combine datasets based on a **common column**.

### **7.2.1 Inner Join (Default)**
Returns only **matching records**.
```python
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [60000, 70000, 80000]})

df_inner = pd.merge(df1, df2, on='ID', how='inner')
print(df_inner)
```
#### **Output**
```
   ID   Name  Salary
0   2    Bob   60000
1   3 Charlie   70000
```
- Only **matching IDs** (2, 3) are retained.

---

### **7.2.2 Left Join (Keeps All Left Table Rows)**
```python
df_left = pd.merge(df1, df2, on='ID', how='left')
print(df_left)
```
#### **Output**
```
   ID   Name  Salary
0   1  Alice     NaN
1   2    Bob  60000.0
2   3 Charlie  70000.0
```
- **All rows from `df1`** are kept.
- **NaN appears** for missing values.

---

### **7.2.3 Right Join (Keeps All Right Table Rows)**
```python
df_right = pd.merge(df1, df2, on='ID', how='right')
print(df_right)
```
#### **Output**
```
   ID   Name  Salary
0   2    Bob   60000
1   3 Charlie   70000
2   4    NaN   80000
```
- **All rows from `df2`** are kept.

---

### **7.2.4 Outer Join (Keeps All Rows from Both Tables)**
```python
df_outer = pd.merge(df1, df2, on='ID', how='outer')
print(df_outer)
```
#### **Output**
```
   ID   Name  Salary
0   1  Alice     NaN
1   2    Bob  60000.0
2   3 Charlie  70000.0
3   4    NaN   80000.0
```
- **All IDs** from both DataFrames are kept.
- **Missing values** are filled with NaN.

---

## **7.3 Joining DataFrames (`df.join()`)**  
`.join()` is used when merging **on the index**.

### **7.3.1 Default Join (Left Join)**
```python
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']}, index=[1, 2, 3])
df2 = pd.DataFrame({'Salary': [60000, 70000, 80000]}, index=[2, 3, 4])

df_join = df1.join(df2)
print(df_join)
```
#### **Output**
```
      Name   Salary
1    Alice      NaN
2      Bob  60000.0
3  Charlie  70000.0
```
- **Left Join by default** (all rows from `df1` kept).
- **Index is used as the key**.

### **7.3.2 Inner Join with `.join()`**
```python
df_inner_join = df1.join(df2, how='inner')
print(df_inner_join)
```
#### **Output**
```
      Name  Salary
2      Bob   60000
3  Charlie   70000
```
- **Only matching indexes are kept**.

---

'''
