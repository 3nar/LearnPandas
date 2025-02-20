


# file name : ExportingProcessedData.py
# Discription : in this file, we will learn Exporting Processed Data
# auther : Nasser hadi
# github : https://github.com/3nar




# Exporting Processed Data in Pandas

'''
# **13. Exporting Processed Data**
After data processing and analysis, it's essential to **save your results** for reporting or future use.  
We will cover:  
✅ **Saving as CSV (`df.to_csv()`)** → Exporting data as CSV files  
✅ **Saving as Excel (`df.to_excel()`)** → Exporting data to Excel files  

---

## **13.1 Saving as CSV (`df.to_csv()`)**  
CSV (Comma-Separated Values) is a common file format for **data storage and transfer**.  

### **13.1.1 Basic Saving to CSV**
```python
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 22],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('output.csv')
```
- By default, this saves:  
  - **All columns** and **rows**  
  - **Index is saved** as a separate column  
  - **Comma (`,`)** as the separator  

---

### **13.1.2 Saving without Index**
To **exclude the index** column:
```python
# Save without index
df.to_csv('output_no_index.csv', index=False)
```

---

### **13.1.3 Saving Specific Columns**
You can save **only selected columns**:
```python
# Save selected columns
df.to_csv('output_selected_columns.csv', columns=['Name', 'Salary'], index=False)
```

---

### **13.1.4 Using a Different Separator (Delimiter)**
You can use a different **delimiter** (e.g., semicolon `;`):
```python
# Save with semicolon delimiter
df.to_csv('output_semicolon.csv', sep=';', index=False)
```

---

### **13.1.5 Handling Missing Values**
If the DataFrame has **missing values** (`NaN`), you can:
- **Replace NaN** with a specific value:
```python
df.to_csv('output_no_nan.csv', index=False, na_rep='N/A')
```

---

### **13.1.6 Saving with Custom Encoding**
If your data contains **special characters**, use UTF-8 encoding:
```python
# Save with UTF-8 encoding
df.to_csv('output_utf8.csv', index=False, encoding='utf-8')
```

---

## **13.2 Saving as Excel (`df.to_excel()`)**  
Pandas allows you to save DataFrames directly to **Excel files**.  
Ensure you have the **openpyxl** package installed:
```bash
pip install openpyxl
```

### **13.2.1 Basic Saving to Excel**
```python
# Save DataFrame to Excel file
df.to_excel('output.xlsx', index=False)
```
- By default, this saves to the **first sheet** in the Excel file.  

---

### **13.2.2 Saving to a Specific Sheet Name**
```python
# Save to a specific sheet
df.to_excel('output_sheet.xlsx', sheet_name='EmployeeData', index=False)
```

---

### **13.2.3 Saving Multiple Sheets**
You can save **multiple DataFrames** to a single Excel file using **ExcelWriter**:
```python
# Sample DataFrames
data2 = {
    'Department': ['HR', 'IT', 'Finance'],
    'Employees': [10, 25, 15]
}
df2 = pd.DataFrame(data2)

# Save multiple sheets
with pd.ExcelWriter('output_multiple_sheets.xlsx') as writer:
    df.to_excel(writer, sheet_name='EmployeeData', index=False)
    df2.to_excel(writer, sheet_name='Departments', index=False)
```

---

### **13.2.4 Formatting NaN Values in Excel**
You can **customize NaN values**:
```python
# Replace NaN with a custom value
df.to_excel('output_nan_custom.xlsx', index=False, na_rep='Missing')
```

---

### **13.2.5 Saving with Custom Encoding**
If your data contains **special characters**, use UTF-8 encoding:
```python
# Save with UTF-8 encoding
df.to_excel('output_utf8.xlsx', index=False, encoding='utf-8')
```

---

### **13.2.6 Saving Excel File with Multiple Index Levels**
If your DataFrame has a **MultiIndex**:
```python
# Creating a MultiIndex DataFrame
arrays = [
    ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Department', 'Employee'))
data = {'Salary': [50000, 60000, 70000, 80000, 55000, 75000]}
df_multi = pd.DataFrame(data, index=index)

# Save MultiIndex DataFrame to Excel
df_multi.to_excel('output_multiindex.xlsx')
```
- The **MultiIndex** is preserved in the Excel file.

---

'''
