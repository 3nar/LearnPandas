


# file name : TimeSeriesData.py
# Discription : in this file, we will learn Working with Time Series Data
# auther : Nasser hadi
# github : https://github.com/3nar




# Working with Time Series Data in Pandas

'''
Pandas provides powerful tools for working with **time series data**, including:  
✅ **Converting to Datetime (`pd.to_datetime()`)** → Converting strings to datetime format  
✅ **Extracting Date Components (`df['Date'].dt.year`)** → Extracting year, month, day, etc.  
✅ **Filtering by Date Range** → Selecting data within a date range  
✅ **Resampling Time Series Data (`df.resample()`)** → Aggregating data over time periods  

---

## **11.1 Converting to Datetime (`pd.to_datetime()`)**  
In Pandas, dates are often stored as strings. You need to **convert them to datetime format** for time series operations.

### **11.1.1 Basic Conversion to Datetime**
```python
import pandas as pd

# Sample DataFrame with date strings
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
    'Sales': [100, 150, 200, 250]
}

df = pd.DataFrame(data)

# Convert to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print(df)
print(df.dtypes)  # Check the data type
```
#### **Output**
```
        Date  Sales
0 2023-01-01    100
1 2023-02-01    150
2 2023-03-01    200
3 2023-04-01    250
Date     datetime64[ns]
Sales             int64
dtype: object
```
- `datetime64[ns]` → Indicates the column is in **datetime format**.

---

### **11.1.2 Converting with a Custom Date Format**
If your date strings have a custom format, use the `format` parameter:
```python
data = {
    'Date': ['01/01/2023', '02/01/2023', '03/01/2023', '04/01/2023'],
    'Sales': [100, 150, 200, 250]
}

df = pd.DataFrame(data)

# Convert using custom date format (MM/DD/YYYY)
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
print(df)
```
#### **Output**
```
        Date  Sales
0 2023-01-01    100
1 2023-02-01    150
2 2023-03-01    200
3 2023-04-01    250
```

---

## **11.2 Extracting Date Components (`df['Date'].dt.year`)**  
Once a column is in datetime format, you can **extract date components** using `.dt`.

### **11.2.1 Extracting Year, Month, and Day**
```python
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print(df)
```
#### **Output**
```
        Date  Sales  Year  Month  Day
0 2023-01-01    100  2023      1    1
1 2023-02-01    150  2023      2    1
2 2023-03-01    200  2023      3    1
3 2023-04-01    250  2023      4    1
```

---

### **11.2.2 Extracting Day Name and Month Name**
```python
df['DayName'] = df['Date'].dt.day_name()
df['MonthName'] = df['Date'].dt.month_name()
print(df)
```
#### **Output**
```
        Date  Sales  Year  Month  Day   DayName MonthName
0 2023-01-01    100  2023      1    1    Sunday   January
1 2023-02-01    150  2023      2    1  Wednesday  February
2 2023-03-01    200  2023      3    1   Wednesday     March
3 2023-04-01    250  2023      4    1   Saturday     April
```

---

## **11.3 Filtering by Date Range**  
You can **filter data** within a specific date range using logical conditions.

### **11.3.1 Filtering Data After a Specific Date**
```python
# Filter rows after March 1, 2023
df_filtered = df[df['Date'] > '2023-03-01']
print(df_filtered)
```
#### **Output**
```
        Date  Sales  Year  Month  Day    DayName MonthName
3 2023-04-01    250  2023      4    1   Saturday     April
```

---

### **11.3.2 Filtering Data Between Two Dates**
```python
# Filter rows between February 1, 2023 and March 31, 2023
df_filtered = df[(df['Date'] >= '2023-02-01') & (df['Date'] <= '2023-03-31')]
print(df_filtered)
```
#### **Output**
```
        Date  Sales  Year  Month  Day     DayName MonthName
1 2023-02-01    150  2023      2    1   Wednesday  February
2 2023-03-01    200  2023      3    1   Wednesday     March
```

---

## **11.4 Resampling Time Series Data (`df.resample()`)**  
`.resample()` is used to **aggregate data over specific time periods**.

### **11.4.1 Setting the Date Column as Index**
Before resampling, set the **Date column as the index**:
```python
df.set_index('Date', inplace=True)
print(df)
```

---

### **11.4.2 Resampling by Month**
```python
# Resample by month and calculate sum of Sales
df_resampled = df['Sales'].resample('M').sum()
print(df_resampled)
```
#### **Output**
```
Date
2023-01-31    100
2023-02-28    150
2023-03-31    200
2023-04-30    250
Freq: M, Name: Sales, dtype: int64
```
- `M` → Monthly resampling  
- `sum()` → Calculates the **total sales per month**  

---

### **11.4.3 Resampling by Quarter**
```python
# Resample by quarter and calculate average Sales
df_resampled_q = df['Sales'].resample('Q').mean()
print(df_resampled_q)
```
#### **Output**
```
Date
2023-03-31    150.0
2023-06-30    250.0
Freq: Q-DEC, Name: Sales, dtype: float64
```
- `Q` → Quarterly resampling  
- `mean()` → Calculates the **average sales per quarter**  

---

'''
