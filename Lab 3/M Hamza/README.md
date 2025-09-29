1.  Assembly Reflections
   
One thing I noticed about Assembly is that everything depends on registers Instructions are very low-level and direct.
Even a small operation like printing to the screen needs several steps, while in Python it’s just one function call.

2.  Python Reflections

Python is easier and faster because it hides the low-level details. 
You don’t need to worry about registers or memory management. Features like variables, functions, and loops make abstraction possible. 
For example, instead of writing several jump instructions for a loop, you just use for or while.

3.  Comparison Table

| Feature | Assembly Example | Python Example | Notes |
| :--- | :--- | :--- | :--- |
| **Variable storage** | Register (EAX) | `x = 5` | In Assembly you deal with registers directly, Python uses variables.  |
| **Printing output** | `INT 21h` | `print()` | Printing in Assembly requires system calls, Python has built-in print(). |
| **Arithmetic** | `ADD AX, BX` | `x + y` | Python loops are simpler and more readable. |
