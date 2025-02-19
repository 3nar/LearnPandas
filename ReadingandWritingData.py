


# file name : ReadingandWritingData.py
# Discription : in this file, we will learn Readingand Writing Data
# auther : Nasser hadi
# github : https://github.com/3nar




# Reading & Writing Data

'''
One of the most powerful features of Pandas is the ability to **read and write data** from different file formats like **CSV, Excel, JSON, and databases**.

---

## **3.1 Reading CSV Files (`pd.read_csv()`)**
A **CSV (Comma-Separated Values)** file is one of the most commonly used formats for data storage.

### **3.1.1 Reading a CSV File**
If you have a CSV file called `data.csv`, you can read it into a Pandas **DataFrame** using:
```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())  # Display the first 5 rows
```
- By default, Pandas assumes the **first row** contains column headers.
- If the file **does not** have headers, use:
```python
df = pd.read_csv('data.csv', header=None)
```

### **3.1.2 Specifying a Column as Index**
You can set a specific column as the **index** while reading:
```python
df = pd.read_csv('data.csv', index_col='ID')
```

### **3.1.3 Handling Missing Data while Reading**
```python
df = pd.read_csv('data.csv', na_values=['NA', 'N/A', 'Missing'])
```

---

## **3.2 Writing to CSV (`df.to_csv()`)**
Once you've processed your data, you can **save it back** as a CSV file.

### **3.2.1 Save DataFrame to CSV**
```python
df.to_csv('output.csv', index=False)  # index=False avoids saving row numbers
```

### **3.2.2 Save DataFrame with a Specific Delimiter**
You can use a different delimiter (e.g., semicolon `;` instead of a comma `,`):
```python
df.to_csv('output_semicolon.csv', sep=';', index=False)
```

---

## **3.3 Reading Excel Files (`pd.read_excel()`)**
Pandas can also read data from **Excel files**.

### **3.3.1 Read an Excel File**
```python
df = pd.read_excel('data.xlsx')
print(df.head())  # Display first 5 rows
```

### **3.3.2 Read a Specific Sheet from an Excel File**
If an Excel file has **multiple sheets**, specify the sheet name:
```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

### **3.3.3 Read an Excel File with a Specific Column as Index**
```python
df = pd.read_excel('data.xlsx', index_col='ID')
```

---

## **3.4 Writing to Excel (`df.to_excel()`)**
### **3.4.1 Save a DataFrame to an Excel File**
```python
df.to_excel('output.xlsx', index=False)
```

### **3.4.2 Save to a Specific Sheet**
```python
df.to_excel('output.xlsx', sheet_name='ProcessedData', index=False)
```

---

'''
