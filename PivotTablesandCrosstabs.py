


# file name : PivotTablesandCrosstabs.py
# Discription : in this file, we will learn Pivot Tables and Crosstabs
# auther : Nasser hadi
# github : https://github.com/3nar




# Pivot Tables & Crosstabs in Pandas

'''
Pivot tables and crosstabs are powerful tools for **data analysis and summarization**.  
We will cover:  
✅ **Creating a Pivot Table (`df.pivot_table()`)** → Summarize data by aggregating values  
✅ **Crosstab for Frequency (`pd.crosstab()`)** → Analyzing frequency distributions  

---

## **9.1 Creating a Pivot Table (`df.pivot_table()`)**  
Pivot tables are useful for **aggregating data** based on **one or more keys**.

### **9.1.1 Basic Pivot Table**
```python
import pandas as pd

# Sample DataFrame
data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 52000, 70000, 80000, 75000, 55000]
}

df = pd.DataFrame(data)

# Creating a basic pivot table
pivot = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print(pivot)
```
#### **Output**
```
               Salary
Department            
Finance     72500.000
HR          52333.333
IT          70000.000
```
- **`values`** → Column to aggregate  
- **`index`** → Rows (group by this column)  
- **`aggfunc`** → Aggregation function (e.g., `mean`, `sum`, `count`)  

---

### **9.1.2 Pivot Table with Multiple Aggregations**
You can calculate **multiple aggregations**:
```python
pivot = df.pivot_table(values='Salary', index='Department', aggfunc=['mean', 'sum', 'max', 'min'])
print(pivot)
```
#### **Output**
```
                  mean     sum    max    min
Department                                  
Finance     72500.000  145000  75000  70000
HR          52333.333  157000  55000  50000
IT          70000.000  140000  80000  60000
```
- Calculates **mean, sum, max, and min** for each department.

---

### **9.1.3 Pivot Table with Multiple Indexes and Columns**
You can **group by multiple keys** and add more **columns**:
```python
pivot = df.pivot_table(values='Salary', index=['Department', 'Gender'], aggfunc='mean')
print(pivot)
```
#### **Output**
```
                        Salary
Department Gender             
Finance    Male      72500.000
HR         Female    52500.000
           Male      52000.000
IT         Female    80000.000
           Male      60000.000
```
- Groups by both `Department` and `Gender`  
- Displays the **average salary** for each group  

---

### **9.1.4 Pivot Table with Columns and Custom Aggregation**
You can display results in **columns**:
```python
pivot = df.pivot_table(values='Salary', index='Department', columns='Gender', aggfunc='mean')
print(pivot)
```
#### **Output**
```
Gender         Female     Male
Department                      
Finance             NaN  72500.0
HR              52500.0  52000.0
IT              80000.0  60000.0
```
- `NaN` means no Female employee in Finance.  

---

## **9.2 Crosstab for Frequency (`pd.crosstab()`)**  
`.crosstab()` is used to **calculate frequencies** or **contingency tables**.

### **9.2.1 Frequency Count**
```python
crosstab = pd.crosstab(df['Department'], df['Gender'])
print(crosstab)
```
#### **Output**
```
Gender      Female  Male
Department               
Finance          0     2
HR               2     1
IT               1     1
```
- Shows the **count** of Male and Female employees per department.

---

### **9.2.2 Percentage Frequency**
You can convert frequencies to **percentages**:
```python
crosstab_percent = pd.crosstab(df['Department'], df['Gender'], normalize='index') * 100
print(crosstab_percent)
```
#### **Output**
```
Gender          Female       Male
Department                        
Finance            0.0      100.0
HR                66.7       33.3
IT                50.0       50.0
```
- **`normalize='index'`** → Normalizes by row (department)  
- **`normalize='columns'`** → Normalizes by column (gender)  

---

### **9.2.3 Crosstab with Multiple Variables**
You can analyze **multiple variables**:
```python
crosstab_multi = pd.crosstab([df['Department'], df['Gender']], df['Salary'])
print(crosstab_multi)
```
#### **Output**
```
Salary                   50000  52000  55000  60000  70000  75000  80000
Department Gender                                                      
Finance    Male               0      0      0      0      1      1      0
HR         Female             1      0      1      0      0      0      0
           Male               0      1      0      0      0      0      0
IT         Female             0      0      0      0      0      0      1
           Male               0      0      0      1      0      0      0
```
- Crosstab of **Salary distribution** by `Department` and `Gender`.

---

'''
