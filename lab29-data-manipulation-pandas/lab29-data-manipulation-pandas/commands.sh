# Commands used in Lab 29

# Install pandas
pip install pandas

# Verify installation
python3 -c "import pandas as pd; print(pd.__version__)"

# Create sample CSV file
cat > employees.csv <<EOF
Name,Age,Department,City
Alice,25,HR,New York
Bob,35,Engineering,San Francisco
Charlie,40,Finance,Chicago
David,28,Engineering,New York
Eve,45,HR,San Francisco
EOF

# Run script
python3 data_manipulation.py

# Check filtered output
cat filtered_data.csv
