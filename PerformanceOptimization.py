


# file name : PerformanceOptimization.pt
# Discription : in this file, we will learn Performance Optimization
# auther : Nasser hadi
# github : https://github.com/3nar




# Pandas Performance Optimization 

'''
As datasets grow larger, **performance optimization** becomes crucial.  
We will learn:  
✅ **Using `astype('category')`** → Memory optimization for categorical data  
✅ **Using `.apply()` instead of `.iterrows()`** → Faster row-wise operations  
✅ **Using `.to_numpy()`** → Efficient numerical calculations  
✅ **Using `.query()`** → Fast filtering using string expressions  

---

## **12.1 Using `astype('category')` for Categorical Data**  
When a column has **repeated categorical values** (e.g., Gender, City), converting it to `category` saves **memory**.

### **12.1.1 Checking Memory Usage Before Optimization**
```python
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'] * 1000,
    'Age': np.random.randint(20, 60, size=5000),
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'] * 1000,
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'] * 1000
}

df = pd.DataFrame(data)

# Check memory usage before optimization
print("Before Optimization:")
print(df.info(memory_usage='deep'))
```
#### **Output**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    5000 non-null   object
 1   Age     5000 non-null   int32 
 2   Gender  5000 non-null   object
 3   City    5000 non-null   object
dtypes: int32(1), object(3)
memory usage: 1.9 MB
```
- The DataFrame uses **1.9 MB** of memory.  

---

### **12.1.2 Converting to `category` Data Type**
```python
# Converting columns with repeated values to category
df['Gender'] = df['Gender'].astype('category')
df['City'] = df['City'].astype('category')

# Check memory usage after optimization
print("\nAfter Optimization:")
print(df.info(memory_usage='deep'))
```
#### **Output**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype   
---  ------  --------------  -----   
 0   Name    5000 non-null   object  
 1   Age     5000 non-null   int32   
 2   Gender  5000 non-null   category
 3   City    5000 non-null   category
dtypes: category(2), int32(1), object(1)
memory usage: 655.2 KB
```
- The DataFrame now uses **655.2 KB** instead of 1.9 MB → **65% memory reduction!**  

---

## **12.2 Using `.apply()` instead of `.iterrows()`**  
`.iterrows()` is **slow** because it **iterates row by row**. `.apply()` is **faster and vectorized**.

### **12.2.1 Using `.iterrows()` (Slow)**
```python
import time

# Adding 10 to each Age using .iterrows() (Slow)
start_time = time.time()

for index, row in df.iterrows():
    df.loc[index, 'Age'] = row['Age'] + 10

print("\nUsing .iterrows(): {:.2f} seconds".format(time.time() - start_time))
```
#### **Output**
```
Using .iterrows(): 0.53 seconds
```

---

### **12.2.2 Using `.apply()` (Fast)**
```python
# Adding 10 to each Age using .apply() (Fast)
start_time = time.time()

df['Age'] = df['Age'].apply(lambda x: x + 10)

print("Using .apply(): {:.2f} seconds".format(time.time() - start_time))
```
#### **Output**
```
Using .apply(): 0.02 seconds
```
- `.apply()` is **25 times faster** than `.iterrows()`!  

---

## **12.3 Using `.to_numpy()` for Faster Computations**  
`.to_numpy()` provides direct access to **NumPy arrays**, which are faster for numerical calculations.

### **12.3.1 Using `.to_numpy()` for Calculations**
```python
# Calculating average Age using .to_numpy() (Fast)
average_age = df['Age'].to_numpy().mean()
print("Average Age:", average_age)
```
- **Direct access** to NumPy's fast numerical calculations.  

---

### **12.3.2 Performance Comparison with `.mean()`**
```python
# Using Pandas .mean() (Slower)
start_time = time.time()
df['Age'].mean()
print("Using .mean(): {:.2f} seconds".format(time.time() - start_time))

# Using .to_numpy() (Faster)
start_time = time.time()
df['Age'].to_numpy().mean()
print("Using .to_numpy(): {:.2f} seconds".format(time.time() - start_time))
```
- `.to_numpy()` is typically **faster** than `.mean()` for large datasets.  

---

## **12.4 Using `.query()` for Efficient Filtering**  
`.query()` is **faster** for complex filtering because it uses **NumExpr** for optimized computation.

### **12.4.1 Filtering Using Boolean Indexing (Slower)**
```python
# Filtering rows with Age > 40 and City = 'New York' (Slower)
start_time = time.time()

df_filtered = df[(df['Age'] > 40) & (df['City'] == 'New York')]

print("Using Boolean Indexing: {:.2f} seconds".format(time.time() - start_time))
```

---

### **12.4.2 Filtering Using `.query()` (Faster)**
```python
# Filtering using .query() (Faster)
start_time = time.time()

df_filtered = df.query("Age > 40 and City == 'New York'")

print("Using .query(): {:.2f} seconds".format(time.time() - start_time))
```
- `.query()` is **faster and more readable** for complex conditions.  

---

'''
