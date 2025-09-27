# Troubleshooting

1. **ModuleNotFoundError: No module named 'openpyxl'**
   - Ensure you installed the dependency: `pip install openpyxl`

2. **FileNotFoundError: mydata.xlsx not found**
   - Make sure to run `create_excel.py` before `read_excel.py`.

3. **PermissionError when saving**
   - Close the file if it is already open in Excel or another program.
