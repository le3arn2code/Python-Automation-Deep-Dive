# Lab 13 – Interview Q&A

**Q1: What is `sys.argv` in Python?**  
A: It is a list containing command-line arguments passed to a script.

**Q2: How do you access the first argument passed to a Python script?**  
A: Using `sys.argv[1]`.

**Q3: What is the difference between `sys.argv` and `argparse`?**  
A: `sys.argv` is basic, while `argparse` provides structured parsing, validation, and help messages.

**Q4: What happens if no arguments are passed with `sys.argv`?**  
A: Only the script name is available in `sys.argv[0]`.

**Q5: What does `argparse.ArgumentParser()` do?**  
A: It creates a parser object to define and manage expected arguments.

**Q6: Can argparse provide default values?**  
A: Yes, using the `default` parameter.

**Q7: How do you define optional arguments in argparse?**  
A: By prefixing them with `--`, e.g., `--age`.

**Q8: How can argparse automatically generate help messages?**  
A: By running `python script.py --help`.

**Q9: What error occurs if required arguments are missing in argparse?**  
A: `SystemExit` error with usage/help message.

**Q10: Why are command-line arguments important?**  
A: They allow flexibility and customization without modifying the code.
