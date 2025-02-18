


# file name : RoadMapPandas.py
# Discription : in this file, we will learn Pandas details , step by step , with a profissonal roadmap
# auther : Nasser hadi
# github : https://github.com/3nar




# Road Map to Learn Pandas

'''
Here's a structured list of everything we covered in Pandas

---

### **1. Introduction to Pandas**
- What is Pandas?
- Installation (`pip install pandas`)
- Importing Pandas (`import pandas as pd`)

---

### **2. Pandas Data Structures**
- **Series (1D array)**
  - Creating a `Series`
  - Custom index in `Series`
- **DataFrame (2D Table)**
  - Creating a `DataFrame` from a dictionary
  - Checking Data (`df.head()`, `df.info()`, `df.describe()`)

---

### **3. Reading & Writing Data**
- Reading CSV (`pd.read_csv()`)
- Writing CSV (`df.to_csv()`)
- Reading Excel (`pd.read_excel()`)
- Writing Excel (`df.to_excel()`)

---

### **4. Selecting & Indexing Data**
- Selecting Columns (`df['ColumnName']`)
- Selecting Rows (`df.loc[]`, `df.iloc[]`)
- Boolean Indexing (`df[df['Age'] > 30]`)

---

### **5. Data Cleaning & Handling Missing Values**
- Checking for missing values (`df.isnull().sum()`)
- Filling missing values (`df.fillna()`)
- Dropping missing values (`df.dropna()`)

---

### **6. Modifying & Transforming Data**
- Adding a new column (`df['NewCol'] = value`)
- Updating column values (`df['Age'] = df['Age'] + 1`)
- Dropping columns (`df.drop(columns=['ColName'])`)
- Dropping rows (`df.drop(index=1)`)
- Changing column names (`df.rename()`)

---

### **7. Merging, Joining, and Concatenation**
- Concatenation (`pd.concat()`)
- Merging (SQL-like joins: `inner`, `left`, `right`, `outer`)
- Joining DataFrames

---

### **8. Grouping & Aggregations**
- Grouping Data (`df.groupby()`)
- Aggregations (`df.agg()`)
- Multi-aggregation (`{'Salary': ['mean', 'max', 'min']}`)

---

### **9. Pivot Tables & Crosstabs**
- Creating a Pivot Table (`df.pivot_table()`)
- Crosstab for frequency (`pd.crosstab()`)

---

### **10. Sorting & Rearranging Data**
- Sorting (`df.sort_values()`)
- Resetting index (`df.reset_index()`)

---

### **11. Working with Time Series Data**
- Converting to datetime (`pd.to_datetime()`)
- Extracting date components (`df['Date'].dt.year`)
- Filtering by date range
- Resampling time series data (`df.resample()`)

---

### **12. Pandas Performance Optimization**
- Using `astype('category')` for categorical data
- Using `.apply()` instead of `.iterrows()`
- Using `.to_numpy()` for faster computations
- Using `.query()` for efficient filtering

---

### **13. Exporting Processed Data**
- Saving as CSV (`df.to_csv()`)
- Saving as Excel (`df.to_excel()`)

---

'''
