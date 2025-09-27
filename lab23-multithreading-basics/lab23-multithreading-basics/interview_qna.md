# Interview Q&A for Lab 23 – Multi-threading Basics

**Q1. What is multi-threading in Python?**  
A: Multi-threading allows concurrent execution of multiple threads within a process.

**Q2. Why use multi-threading?**  
A: To improve efficiency and responsiveness, especially with I/O-bound tasks.

**Q3. How do you create a thread in Python?**  
A: Using `threading.Thread(target=function, args=(...))`.

**Q4. What does `join()` do for threads?**  
A: It makes the main program wait until the thread finishes execution.

**Q5. What happens if we don’t call `join()`?**  
A: The program may exit before threads complete.

**Q6. How does Python handle concurrency with threads?**  
A: Python threads run concurrently but are limited by the Global Interpreter Lock (GIL).

**Q7. When should you avoid using threads?**  
A: For CPU-bound tasks; use multiprocessing instead.

**Q8. Can threads share data?**  
A: Yes, threads share memory space, but this can lead to race conditions if not managed properly.

**Q9. Give an example use case of multi-threading.**  
A: Web servers handling multiple client requests simultaneously.

**Q10. What is the difference between concurrency and parallelism?**  
A: Concurrency is interleaved task execution; parallelism is true simultaneous execution on multiple cores.
