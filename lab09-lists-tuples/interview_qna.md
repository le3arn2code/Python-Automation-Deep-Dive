# Interview Q&A – Lab 9 (Lists and Tuples)

1. **Q:** What is the difference between a list and a tuple in Python?  
   **A:** Lists are mutable, tuples are immutable.

2. **Q:** Which data structure is faster for iteration, lists or tuples?  
   **A:** Tuples are slightly faster because they are immutable.

3. **Q:** Can a tuple contain a list?  
   **A:** Yes, and the list inside can still be modified.

4. **Q:** How do you convert a list to a tuple?  
   **A:** Use tuple(my_list).

5. **Q:** How do you convert a tuple to a list?  
   **A:** Use list(my_tuple).

6. **Q:** Can tuples be used as dictionary keys? Why?  
   **A:** Yes, because they are immutable and hashable.

7. **Q:** Can lists be used as dictionary keys?  
   **A:** No, because they are mutable and not hashable.

8. **Q:** How do you sort a list in Python?  
   **A:** Use .sort() or sorted(list).

9. **Q:** What happens if you try to remove a non-existing element from a list?  
   **A:** Python raises a ValueError.

10. **Q:** When should you use a tuple instead of a list?  
    **A:** When you need fixed data that should not change (e.g., coordinates, constants).
