# Troubleshooting

- **Issue:** ImportError: No module named requests  
  **Fix:** Install the library with `pip install requests`.

- **Issue:** Network error or timeout.  
  **Fix:** Ensure internet connectivity, check API endpoint.

- **Issue:** No data written to CSV.  
  **Fix:** Confirm filter condition matches records.

- **Issue:** Unicode encoding error when saving CSV.  
  **Fix:** Use `encoding="utf-8"` in file handling.

- **Issue:** CLI arguments not recognized.  
  **Fix:** Ensure correct syntax, e.g. `python3 fetch_data.py --user_id 2`.
