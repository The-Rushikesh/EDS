import pandas as pd

# === Ensure all columns display fully ===
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# === Load the dataset ===
df = pd.read_csv('wheat.csv')
print("=== Dataset Overview ===")
print(df.head())

# 1. Show the first 10 grains (data entries)
print("\n1. First 10 grains:")
print(df.head(10))

# 2. Find the total number of grains in the dataset
total_grains = len(df)
print("\n2. Total number of grains in dataset:", total_grains)

# 3. Check for any missing (null) values in the dataset
print("\n3. Missing values in each column:")
print(df.isnull().sum())

# 4. Find the average (mean) of each numeric feature
print("\n4. Mean of each numeric column:")
print(df.mean(numeric_only=True))

# 5. Identify how many unique categories are in the dataset
if 'category' in df.columns:
    unique_categories = df['category'].nunique()
    print("\n5. Number of unique categories:", unique_categories)
else:
    print("\n5. Column 'category' not found in dataset.")

# 6. Count how many grains belong to each category
if 'category' in df.columns:
    print("\n6. Count of grains per category:")
    print(df['category'].value_counts())
else:
    print("\n6. Column 'category' not found in dataset.")

# 7. Find the grain with the maximum area
if 'area' in df.columns:
    print("\n7. Grain with maximum area:")
    print(df[df['area'] == df['area'].max()])
else:
    print("\n7. Column 'area' not found in dataset.")

# 8. Filter and show all grains where length > 6.0
if 'length' in df.columns:
    print("\n8. Grains with length > 6.0:")
    print(df[df['length'] > 6.0])
else:
    print("\n8. Column 'length' not found in dataset.")

# 9. Sort the grains by perimeter in descending order
if 'perimeter' in df.columns:
    print("\n9. Grains sorted by perimeter (descending):")
    print(df.sort_values(by='perimeter', ascending=False))
else:
    print("\n9. Column 'perimeter' not found in dataset.")

# 10. Create a new column: length-to-width ratio
if 'length' in df.columns and 'width' in df.columns:
    df['length_to_width_ratio'] = df['length'] / df['width']
    print("\n10. Length to width ratio (first 5 rows):")
    print(df[['length', 'width', 'length_to_width_ratio']].head())
else:
    print("\n10. Required columns for ratio not found in dataset.")
