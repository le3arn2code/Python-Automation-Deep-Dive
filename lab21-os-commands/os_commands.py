import subprocess

# Run a basic OS command (Linux/macOS: ls -l, Windows: dir)
try:
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True)  # For Linux/macOS
    # result = subprocess.run(['dir'], shell=True, capture_output=True, text=True)  # For Windows

    print("Standard Output:")
    print(result.stdout)

    print("Standard Error (if any):")
    print(result.stderr)

    if result.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Command failed with exit code:", result.returncode)

except subprocess.CalledProcessError as e:
    print("An error occurred:", e)
