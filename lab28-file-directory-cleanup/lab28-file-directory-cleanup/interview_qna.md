# Interview Q&A – Lab 28

**Q1.** What Python modules are used for file cleanup?  
**A1.** `os` for file operations, `time` for timestamps, and `logging` for logs.

**Q2.** How does Python determine file age?  
**A2.** By subtracting file modification time (`os.path.getmtime`) from current epoch time.

**Q3.** What is the advantage of a dry-run mode?  
**A3.** It prevents accidental deletions by previewing which files would be removed.

**Q4.** How can you recursively clean subdirectories?  
**A4.** Use `os.walk()` instead of `os.listdir()`.

**Q5.** What happens if the script tries to delete a directory?  
**A5.** With `os.path.isfile()` check, directories are skipped.

**Q6.** How can you avoid deleting critical files?  
**A6.** Add exclusions by filename, extension, or path checks.

**Q7.** Why use logging instead of only printing to console?  
**A7.** Logs provide persistent audit trails for compliance and debugging.

**Q8.** How can you schedule this cleanup script?  
**A8.** Use cron jobs (Linux) or Task Scheduler (Windows).

**Q9.** How do you test this script safely?  
**A9.** With dry-run mode and backdated test files.

**Q10.** How can this be extended for enterprise use?  
**A10.** Add archiving instead of deleting, recursive scanning, cloud storage integration, and reporting dashboards.
