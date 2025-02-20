


# file name : SortingandRearrangingData.py
# Discription : in this file, we will learn Sorting and Rearranging Data
# auther : Nasser hadi
# github : https://github.com/3nar




# Sorting & Rearranging Data in Pandas

'''
Sorting and rearranging data is crucial for **data analysis, reporting, and visualization**.  
We will cover:  
✅ **Sorting (`df.sort_values()`)** → Sorting rows by column values  
✅ **Resetting Index (`df.reset_index()`)** → Resetting or rearranging the index  

---

## **10.1 Sorting Data (`df.sort_values()`)**  
`.sort_values()` is used to **sort rows** by one or more columns.  

### **10.1.1 Sorting by a Single Column (Ascending Order)**
```python
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 22],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df = pd.DataFrame(data)

# Sorting by Age (Ascending by default)
df_sorted = df.sort_values(by='Age')
print(df_sorted)
```
#### **Output**
```
       Name  Age  Salary
4       Eve   22   55000
0     Alice   25   50000
1       Bob   30   60000
2   Charlie   35   70000
3     David   40   80000
```
- Sorted by **Age** in **ascending** order.  

---

### **10.1.2 Sorting by a Single Column (Descending Order)**
```python
# Sorting by Salary (Descending Order)
df_sorted_desc = df.sort_values(by='Salary', ascending=False)
print(df_sorted_desc)
```
#### **Output**
```
       Name  Age  Salary
3     David   40   80000
2   Charlie   35   70000
1       Bob   30   60000
4       Eve   22   55000
0     Alice   25   50000
```
- Sorted by **Salary** in **descending** order.  

---

### **10.1.3 Sorting by Multiple Columns**
You can sort by **multiple columns**:
```python
# Sorting by Age (ascending) and then by Salary (descending)
df_sorted_multi = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
print(df_sorted_multi)
```
#### **Output**
```
       Name  Age  Salary
4       Eve   22   55000
0     Alice   25   50000
1       Bob   30   60000
2   Charlie   35   70000
3     David   40   80000
```
- Sorted by `Age` in **ascending order**  
- If `Age` is the same, then sorted by `Salary` in **descending order**  

---

### **10.1.4 Sorting by Index (`df.sort_index()`)**
You can sort the DataFrame by **index**:
```python
# Sort by index
df_sorted_index = df.sort_index()
print(df_sorted_index)
```
- This sorts the DataFrame **by its index**.

---

## **10.2 Resetting Index (`df.reset_index()`)**  
If you sort or filter rows, the **index** may become disorganized.  
`.reset_index()` is used to **reset the index**.

### **10.2.1 Reset Index After Sorting**
```python
# Sorting by Age (Descending)
df_sorted = df.sort_values(by='Age', ascending=False)

# Reset index after sorting
df_reset = df_sorted.reset_index(drop=True)
print(df_reset)
```
#### **Output**
```
       Name  Age  Salary
0     David   40   80000
1   Charlie   35   70000
2       Bob   30   60000
3     Alice   25   50000
4       Eve   22   55000
```
- **`drop=True`** → Drops the old index (avoiding an additional column)  
- **`drop=False`** → Keeps the old index as a new column  

---

### **10.2.2 Reset Index After Filtering**
If you **filter rows**, the index might be disorganized:
```python
# Filtering rows where Salary > 60000
df_filtered = df[df['Salary'] > 60000]

# Reset index after filtering
df_reset = df_filtered.reset_index(drop=True)
print(df_reset)
```
#### **Output**
```
       Name  Age  Salary
0   Charlie   35   70000
1     David   40   80000
```
- The index is reset **sequentially** (0, 1, 2, ...).

---

### **10.2.3 Reset Index and Keep Old Index**
You can keep the **old index** as a new column:
```python
df_reset_keep = df_filtered.reset_index(drop=False)
print(df_reset_keep)
```
#### **Output**
```
   index      Name  Age  Salary
0      2   Charlie   35   70000
1      3     David   40   80000
```
- The **old index** is preserved as a new column called `index`.  

---

'''
