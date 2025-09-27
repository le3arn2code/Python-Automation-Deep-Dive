# Troubleshooting Lab 23

1. **Issue:** Python script not running.
   - **Fix:** Ensure Python 3 is installed. Run `python3 --version`.

2. **Issue:** Module `threading` not found.
   - **Fix:** The `threading` module is built-in. Ensure correct Python environment.

3. **Issue:** Output not interleaved as expected.
   - **Fix:** This can vary depending on CPU scheduling; rerun the program multiple times.

4. **Issue:** Script stuck without finishing.
   - **Fix:** Ensure `thread1.join()` and `thread2.join()` are included so main thread waits.
