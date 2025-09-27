# Interview Q&A – Lab 20 Sending Emails

**Q1: What is smtplib in Python?**
A: A built-in module used to send emails via the Simple Mail Transfer Protocol.

**Q2: Which port is commonly used for SMTP with TLS?**
A: Port 587.

**Q3: Why use starttls()?**
A: It upgrades an insecure connection to a secure TLS/SSL connection.

**Q4: What are MIME types in emails?**
A: Multipurpose Internet Mail Extensions, used to send text, HTML, attachments, etc.

**Q5: How do you avoid hardcoding credentials in scripts?**
A: Use environment variables or secret managers.

**Q6: What happens if you skip server.quit()?**
A: The SMTP connection may remain open, leading to resource leaks.

**Q7: What are less secure app settings in Gmail?**
A: A toggle that allows older authentication methods (deprecated).

**Q8: What’s the secure alternative to less secure apps?**
A: App-specific passwords or OAuth2.

**Q9: How do you send attachments via smtplib?**
A: Use `email.mime.multipart.MIMEMultipart` and attach files.

**Q10: Can smtplib be used for production apps?**
A: Yes, but always with secure credentials handling (OAuth, app passwords).
