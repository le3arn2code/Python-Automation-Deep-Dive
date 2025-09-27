# Troubleshooting

- **Issue:** ImportError: No module named pandas  
  **Fix:** Ensure pandas is installed using `pip install pandas`.

- **Issue:** FileNotFoundError when reading CSV.  
  **Fix:** Ensure the CSV file exists in the correct directory or provide full path.

- **Issue:** Filtered DataFrame is empty.  
  **Fix:** Verify the column name is correct and that conditions match some rows.

- **Issue:** Extra index column in CSV output.  
  **Fix:** Use `index=False` in `to_csv()` to avoid writing the index.
