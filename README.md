# Python Multiprocessing Pool Tasks

This repository contains beginner-friendly Python programs demonstrating the use of the `multiprocessing` module, `Pool`, and `Pool.map()` for performing numerical computations using multiple processes.

## Programs Included

1. **Sum of Even Numbers**
   - Calculates the sum of all even numbers from 1 to N.
   - Processes multiple input values using `Pool.map()`.
   - Displays the Process ID, input number, and calculated sum.

2. **Sum of Odd Numbers**
   - Calculates the sum of all odd numbers from 1 to N.
   - Uses multiple worker processes for different input values.

3. **Count Even Numbers**
   - Counts how many even numbers exist between 1 and N.
   - Executes the task for multiple values using `Pool.map()`.

4. **Count Odd Numbers**
   - Counts how many odd numbers exist between 1 and N.
   - Displays the Process ID, input number, and odd number count.

5. **Parallel Factorials**
   - Calculates factorials of multiple numbers using `multiprocessing.Pool`.
   - Displays the Process ID, input number, and factorial result.

## Concepts Practiced

- Python Multiprocessing
- `multiprocessing.Pool`
- `Pool.map()`
- Worker Processes
- Process IDs using `os.getpid()`
- Parallel Execution
- Functions
- Loops
- Even and Odd Number Logic
- Factorial Calculation

## Requirements

- Python 3

No external libraries are required.

## Purpose

This repository is part of my Python learning journey and focuses on understanding parallel execution and numerical computations using `multiprocessing.Pool` and `Pool.map()`.
