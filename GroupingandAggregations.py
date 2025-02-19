


# file name : GroupingandAggregations.pt
# Discription : in this file, we will learn Grouping and Aggregations
# auther : Nasser hadi
# github : https://github.com/3nar




# Grouping & Aggregations in Pandas

'''
Grouping and aggregations allow you to **analyze and summarize** your dataset efficiently.  
We will cover:  
✅ **Grouping Data (`df.groupby()`)** → Organizing data based on a column  
✅ **Aggregations (`df.agg()`)** → Performing calculations like sum, mean, max, etc.  
✅ **Multi-aggregation (`{'Salary': ['mean', 'max', 'min']}`)** → Applying multiple aggregations  

---

## **8.1 Grouping Data (`df.groupby()`)**  
The `.groupby()` function allows you to **group rows based on a column**.

### **8.1.1 Grouping and Applying a Single Aggregation**  
Let's create a dataset:
```python
import pandas as pd

# Sample DataFrame
data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Salary': [50000, 60000, 52000, 70000, 80000, 75000, 55000]
}

df = pd.DataFrame(data)

# Group by Department and calculate the average salary
df_grouped = df.groupby('Department')['Salary'].mean()
print(df_grouped)
```
#### **Output**
```
Department
Finance    72500.0
HR         52333.3
IT         70000.0
Name: Salary, dtype: float64
```
- Groups employees by **Department** and **calculates the mean salary**.

---

### **8.1.2 Grouping and Applying Multiple Aggregations**
You can apply multiple **aggregations (sum, mean, max, min, count, etc.)**:
```python
df_grouped = df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'sum', 'count'])
print(df_grouped)
```
#### **Output**
```
             mean    max    min     sum  count
Department                                    
Finance  72500.0  75000  70000  145000      2
HR       52333.3  55000  50000  157000      3
IT       70000.0  80000  60000  140000      2
```
- **`mean`** → Average salary per department  
- **`max`** → Maximum salary per department  
- **`min`** → Minimum salary per department  
- **`sum`** → Total salary per department  
- **`count`** → Number of employees per department  

---

## **8.2 Aggregations (`df.agg()`)**
Instead of using `.groupby()`, we can apply aggregations directly on the whole DataFrame.

### **8.2.1 Single Aggregation on a Column**
```python
print(df['Salary'].agg('mean'))  # Calculate mean salary
```
#### **Output**
```
63000.0
```

### **8.2.2 Multiple Aggregations**
```python
print(df['Salary'].agg(['mean', 'sum', 'max', 'min']))
```
#### **Output**
```
mean    63000.0
sum    441000.0
max    80000.0
min    50000.0
Name: Salary, dtype: float64
```

---

## **8.3 Multi-aggregation (`df.groupby().agg()` with dictionary)**
To apply **different functions to different columns**, use a dictionary inside `.agg()`.

```python
df_grouped = df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min'],
    'Employee': 'count'  # Count employees per department
})
print(df_grouped)
```
#### **Output**
```
             Salary                   Employee
               mean    max    min  count
Department                                
Finance  72500.0  75000  70000      2
HR       52333.3  55000  50000      3
IT       70000.0  80000  60000      2
```
- `Salary`: Applies **mean, max, min**  
- `Employee`: Counts the number of employees in each department  

---

'''
