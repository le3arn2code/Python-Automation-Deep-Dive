import pandas as pd

# Step 1: Read CSV file
df = pd.read_csv('employees.csv')
print("Original Data:")
print(df.head())

# Step 2: Filter rows (Age > 30)
filtered_df = df[df['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_df)

# Step 3: Save filtered data to new CSV
filtered_df.to_csv('filtered_data.csv', index=False)
print("\nFiltered data saved to filtered_data.csv")
