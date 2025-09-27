# Interview Q&A – Lab 22

**Q1: What is cron used for?**  
A: Cron automates repetitive tasks by scheduling commands/scripts to run at specified times.

**Q2: How do you check if cron is working?**  
A: Use `systemctl status cron` or check logs with `grep CRON /var/log/syslog`.

**Q3: Difference between cron and anacron?**  
A: Cron runs tasks at scheduled times, anacron ensures tasks are run even if the system was off at the scheduled time.

**Q4: Common cron expression for every minute?**  
A: `* * * * *`

**Q5: How to ensure Python script works with cron?**  
A: Use absolute paths for both Python binary and script.

**Q6: Where is cron configuration stored?**  
A: In `/etc/crontab` and user crontabs (`crontab -e`).

**Q7: How do you test a scheduled script manually?**  
A: Run the script directly with Python before scheduling.

**Q8: What does `tail -f log.txt` do?**  
A: Continuously monitors the file for new appended lines.

**Q9: How does Task Scheduler differ from cron?**  
A: Task Scheduler is GUI-based and Windows-specific, cron is CLI-based and Unix/Linux specific.

**Q10: Why avoid relative paths in cron jobs?**  
A: Because cron may run in a different working directory; absolute paths prevent errors.
