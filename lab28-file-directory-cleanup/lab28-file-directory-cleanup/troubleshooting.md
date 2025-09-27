# Troubleshooting

- **Issue:** Script deletes nothing.  
  **Fix:** Files may not meet the age threshold. Use `touch -d "60 days ago"` to backdate files or lower the threshold in the script.

- **Issue:** Permission denied when deleting files.  
  **Fix:** Run with appropriate permissions or change file ownership.

- **Issue:** Log file not updating.  
  **Fix:** Ensure logging configuration is correct and file is writable.
