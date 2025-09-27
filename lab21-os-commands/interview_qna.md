# Interview Q&A – Lab 21 Automation with OS Commands

### Q1: What is the subprocess module in Python?
A: It allows execution of OS-level commands from within Python scripts.

### Q2: Difference between os.system() and subprocess.run()?
A: os.system() executes a command but does not capture output. subprocess.run() provides more control and captures output.

### Q3: How do you capture both stdout and stderr in subprocess?
A: Use `capture_output=True` or explicitly pass `stdout=subprocess.PIPE, stderr=subprocess.PIPE`.

### Q4: What does returncode represent in subprocess?
A: It indicates success (0) or failure (non-zero) of the executed command.

### Q5: Why use try-except with subprocess?
A: To handle exceptions such as CalledProcessError when commands fail.

### Q6: How can you run Windows commands using subprocess?
A: Use `subprocess.run(['dir'], shell=True, capture_output=True, text=True)`.

### Q7: What happens if the command is not found?
A: subprocess raises a FileNotFoundError or CalledProcessError.

### Q8: How to run multiple commands sequentially?
A: Either call subprocess multiple times or use `&&` inside the command string.

### Q9: Why should you avoid shell=True when possible?
A: It may introduce security risks (command injection).

### Q10: How can subprocess improve automation workflows?
A: It integrates Python with OS commands, enabling scripting, automation, and DevOps tasks.
