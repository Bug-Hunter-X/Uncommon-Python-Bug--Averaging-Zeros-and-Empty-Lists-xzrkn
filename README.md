# Python Bug: Average Calculation
This repository contains a Python script demonstrating an edge case in average calculation, along with a solution.

The `bug.py` file shows a simple function to calculate the average of a list of numbers.  This version handles empty lists by returning 0, but this may not be ideal for all applications.  In particular, it does not raise an error for an empty list and will happily average lists composed entirely of zeros (resulting in an average of 0).

The improved `bugSolution.py` file addresses this by incorporating additional checks and exception handling.  This ensures more robust behavior.

## Issues Addressed
* **Empty Lists:** The original implementation returns 0 for empty lists. The improved version raises a ValueError for a more informative error handling. 
* **All Zeros:** The original implementation returns 0 if all numbers are 0. This is technically correct but might not be the desired behavior in every case.  The improved version can be modified to handle this differently based on user needs (i.e., raising an error or returning a specific value).

## How to Use
1. Clone the repository
2. Run `bug.py` to see the original implementation and its behavior with different input cases.
3. Run `bugSolution.py` to see the improved, more robust version. 