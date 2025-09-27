# Troubleshooting – Lab 22

- **Script not running?**
  - Ensure correct Python path in crontab: `/usr/bin/python3 /home/user/time_logger.py`
  - Verify cron service is running: `systemctl status cron`

- **No updates in log.txt?**
  - Check script permissions: `chmod +x time_logger.py`
  - Review cron logs: `grep CRON /var/log/syslog` (Linux)

- **Windows Task Scheduler issues**
  - Ensure correct path to Python and script.
  - Check Task Scheduler history for errors.
