# Lab 18 – Interview Q&A

1. Q: What is the purpose of the requests module?
   A: It allows Python programs to send HTTP/HTTPS requests easily.

2. Q: Difference between requests.get() and requests.post()?
   A: GET retrieves data, POST sends data to the server.

3. Q: How do you check if a request was successful?
   A: Check if response.status_code == 200.

4. Q: How do you parse JSON from a response?
   A: Use response.json().

5. Q: What does response.text return?
   A: Raw text of the response body.

6. Q: What happens if the API returns HTML instead of JSON?
   A: response.json() will raise a JSONDecodeError.

7. Q: Can requests handle timeouts?
   A: Yes, use requests.get(url, timeout=5).

8. Q: How do you send headers with a request?
   A: Pass headers as a dictionary, e.g., requests.get(url, headers={"User-Agent": "myApp"}).

9. Q: How do you handle authentication in requests?
   A: Use requests.get(url, auth=(user, pass)).

10. Q: Why use requests over urllib?
    A: Simpler syntax, more features, and better usability.
