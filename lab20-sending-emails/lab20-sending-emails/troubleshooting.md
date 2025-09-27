# Troubleshooting – Lab 20 Sending Emails

1. **Authentication Error (535, 534, etc.)**
   - Cause: Wrong username/password or insecure app settings.
   - Fix: Enable "Allow less secure apps" (testing only) or use app-specific password.

2. **Connection Refused**
   - Cause: Wrong SMTP server or port.
   - Fix: Check correct SMTP server and port (Gmail: smtp.gmail.com:587).

3. **TLS/SSL Errors**
   - Cause: Missing `starttls()` call.
   - Fix: Ensure `server.starttls()` is executed before login.
