


# file name : ModifyingandTransformingData.py
# Discription : in this file, we will learn Modifying & Transforming Data
# auther : Nasser hadi
# github : https://github.com/3nar




# Modifying & Transforming Data in Pandas

'''
Data modification and transformation are essential for data cleaning, feature engineering, and analysis. Let's explore how to add, update, drop, and rename columns/rows.

6.1 Adding a New Column (df['NewCol'] = value)


6.1.1 Adding a Column with Fixed Values

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Add a new column with a fixed value
df['Country'] = 'USA'
print(df)

Output

     Name  Age         City Country
0   Alice   25     New York     USA
1     Bob   30  Los Angeles     USA
2  Charlie   35     Chicago     USA


6.1.2 Adding a Column with Calculated Values


You can create a new column based on existing ones.
df['Age in 5 Years'] = df['Age'] + 5


6.1.3 Adding a Column Using a Function (apply())


df['Age Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
print(df)

Output

     Name  Age         City Country  Age Group
0   Alice   25     New York     USA      Young
1     Bob   30  Los Angeles     USA      Adult
2  Charlie   35     Chicago     USA      Adult


6.2 Updating Column Values (df['ColumnName'] = new_values)


6.2.1 Updating a Column's Values

df['Age'] = df['Age'] + 1  # Increase all ages by 1

6.2.2 Updating Specific Rows

df.loc[df['Name'] == 'Alice', 'Age'] = 28  # Update Alice's age

6.2.3 Updating Multiple Columns

df[['Age', 'Age in 5 Years']] = df[['Age', 'Age in 5 Years']] + 2  # Add 2 to both columns


6.3 Dropping Columns (df.drop(columns=['ColName']))

6.3.1 Dropping a Single Column

df = df.drop(columns=['Country'])

6.3.2 Dropping Multiple Columns

df = df.drop(columns=['Age in 5 Years', 'Age Group'])


6.4 Dropping Rows (df.drop(index=value))

6.4.1 Dropping a Specific Row

df = df.drop(index=1)  # Drop the row with index 1

6.4.2 Dropping Multiple Rows

df = df.drop(index=[0, 2])  # Drop rows with index 0 and 2

6.4.3 Dropping Rows Based on a Condition

df = df[df['Age'] > 25]  # Keep only rows where Age > 25

6.5 Changing Column Names (df.rename())


6.5.1 Renaming Specific Columns

df = df.rename(columns={'Name': 'Full Name', 'Age': 'Years'})
print(df)

Output

   Full Name  Years         City
0     Alice     25     New York
1       Bob     30  Los Angeles
2   Charlie     35     Chicago


6.5.2 Renaming All Columns

df.columns = ['Customer Name', 'Customer Age', 'Customer City']

---

'''
