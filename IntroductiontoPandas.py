


# file name : IntroductiontoPandas.py
# Discription : in this file, we will learn Introduction to Pandas
# auther : Nasser hadi
# github : https://github.com/3nar




# Introduction to Pandas

'''

Pandas is a **powerful** Python library for data analysis and manipulation. It is widely used in data science, machine learning, and data engineering.

---

## **1.1 What is Pandas?**
Pandas provides **data structures and tools** to manipulate structured data efficiently.

### **Key Features of Pandas:**
✅ **Easy Data Handling:** Works well with structured data (e.g., tables, Excel files, databases).  
✅ **Powerful Data Structures:** Supports **Series (1D)** and **DataFrame (2D)** structures.  
✅ **Data Cleaning & Transformation:** Handles missing values, filtering, sorting, and grouping.  
✅ **Integration with Other Libraries:** Works well with NumPy, Matplotlib, Scikit-learn, and more.  
✅ **Fast Performance:** Optimized for handling large datasets efficiently.  

### **Where is Pandas Used?**
- Data analysis and visualization
- Machine learning preprocessing
- Financial and business analytics
- Working with databases and big data

---

## **1.2 Installation of Pandas**
To use Pandas, you need to install it first. You can do this using **pip**:

### **Install Pandas**
Open your **command line (cmd, terminal, or PowerShell)** and type:
```bash
pip install pandas
```

If you are using **Anaconda**, install it using:
```bash
conda install pandas
```

### **Verify Installation**
After installation, open **Python** and type:
```python
import pandas as pd
print(pd.__version__)  # Check installed version
```
If Pandas is installed correctly, this should print the installed version.

---

## **1.3 Importing Pandas**
Once installed, you must import Pandas into your Python script:

```python
import pandas as pd
```
Here, we import Pandas with the alias **pd** (a common convention to keep the code short).

---

## **1.4 Setting Up Git for Pandas Projects**
Using **Git** will help track changes and manage code versions.

### **Step 1: Install Git (If Not Installed)**
Check if Git is installed:
```bash
git --version
```
If Git is not installed, download it from [git-scm.com](https://git-scm.com/).

### **Step 2: Set Up Git**
After installation, configure your Git username and email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### **Step 3: Create a Git Repository for Pandas**
Navigate to your project folder and initialize a Git repository:
```bash
mkdir pandas-learning  # Create a new folder
cd pandas-learning  # Enter the folder
git init  # Initialize Git
```

### **Step 4: Create a Python Script**
Inside `pandas-learning`, create a new Python script (`pandas_intro.py`):
```bash
touch pandas_intro.py  # For Mac/Linux
echo > pandas_intro.py  # For Windows
```
Then, open the file and add:
```python
import pandas as pd
print("Pandas Imported Successfully!")
```

'''
