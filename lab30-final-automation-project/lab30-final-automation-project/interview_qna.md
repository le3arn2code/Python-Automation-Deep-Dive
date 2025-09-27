# Interview Q&A – Lab 30

**Q1.** What library is used to fetch API data in Python?  
**A1.** The `requests` library.

**Q2.** How do you handle errors from API requests?  
**A2.** Using `try/except` with `response.raise_for_status()`.

**Q3.** Why use logging instead of print statements?  
**A3.** Logging provides persistent, timestamped records useful for debugging and audits.

**Q4.** What module helps with command-line arguments?  
**A4.** The `argparse` module.

**Q5.** How do you write dictionaries to a CSV file?  
**A5.** Use `csv.DictWriter` with `writerow()`.

**Q6.** Why use CLI arguments in automation?  
**A6.** They make the script flexible and reusable without editing code.

**Q7.** How does Python parse JSON data?  
**A7.** With `response.json()` method in `requests`.

**Q8.** What happens if API returns non-200 response?  
**A8.** `raise_for_status()` throws an exception, caught in error handling.

**Q9.** What is the advantage of modularizing fetch, process, and save?  
**A9.** Improves readability, testing, and reusability.

**Q10.** How can this lab be extended?  
**A10.** Add scheduling, database integration, email notifications, or advanced analytics.
