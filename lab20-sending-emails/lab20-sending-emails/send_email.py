import smtplib
import os
from email.mime.text import MIMEText

smtp_server = os.getenv("LAB20_SMTP_SERVER")
smtp_port = int(os.getenv("LAB20_SMTP_PORT", 587))
email_user = os.getenv("LAB20_SMTP_USER")
email_password = os.getenv("LAB20_SMTP_PASSWORD")
recipient_email = os.getenv("LAB20_RECIPIENT")

subject = "Lab 20 Test Email"
body = "This is a test email sent from send_email.py (Lab 20)."

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = email_user
msg['To'] = recipient_email

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, recipient_email, msg.as_string())
    print("Email sent successfully!")
    server.quit()
except Exception as e:
    print(f"An error occurred: {e}")
