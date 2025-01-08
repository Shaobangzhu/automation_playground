# Recursion I and Binary Search Tree
## 1. 表象上: function calls itself
## 2. 实质上: Boil down a big problem to smaller ones (size n depends on size n - 1, or n - 2 or ... n/2)
## 3. Implementation上：
### a. Base case: smallest problem to solve
### b. Recursive rule: how to make the problem smaller (if we can resolve the same problem but with a smaller size, then what is left to do for the current problem size n)