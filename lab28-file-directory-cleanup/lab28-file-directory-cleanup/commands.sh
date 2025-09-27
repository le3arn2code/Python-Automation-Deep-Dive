# Commands used in Lab 28

# Create directory and test files
mkdir FileCleanupLab
cd FileCleanupLab
mkdir test_directory
touch test_directory/old_file1.txt
touch test_directory/new_file.txt

# Backdate file for testing
touch -d "60 days ago" test_directory/old_file1.txt

# Run script (dry run mode)
python3 cleanup_script.py

# View logs
cat cleanup_log.txt
