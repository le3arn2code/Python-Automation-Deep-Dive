# Interview Q&A - Lab 27 API Automation

**Q1: What is the purpose of the requests library in Python?**
A1: It simplifies sending HTTP/1.1 requests, such as GET and POST, without manually handling sockets.

**Q2: Why use POST instead of GET in APIs?**
A2: POST is used for sending data securely in the request body, while GET appends data to the URL.

**Q3: How do you check if an HTTP request was successful?**
A3: By checking `response.status_code == 200`.

**Q4: What is the difference between response.text and response.json()?**
A4: `response.text` gives raw string output, while `response.json()` parses JSON into a Python dictionary.

**Q5: What are common status codes in API responses?**
A5: 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error).

**Q6: Why use a service like httpbin.org for API testing?**
A6: It provides a safe testing environment that echoes requests for debugging.

**Q7: How would you secure API requests in production?**
A7: Use HTTPS, authentication tokens, and avoid logging sensitive data.

**Q8: What is JSON and why is it commonly used in APIs?**
A8: JSON (JavaScript Object Notation) is a lightweight data-interchange format, easy for humans to read and machines to parse.

**Q9: How do you handle API rate limits?**
A9: Implement retries with exponential backoff and respect the API’s usage guidelines.

**Q10: Can you send files with requests.post()?**
A10: Yes, by using the `files` parameter, e.g., `requests.post(url, files={'file': open('test.txt','rb')})`.
