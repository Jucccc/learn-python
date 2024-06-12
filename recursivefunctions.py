
import sys

# Find out n factorial - recursive way:
# Requires more memory
# Recursion is practically a faster method for applications
# like traversing trees and binary search.
def rec_fact(n):
    if n == 0:
        return 1
    return n * rec_fact(n-1)
print(rec_fact(5))

# Normal way:
def iter_fact(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
print(iter_fact(5))

# Is there any recursion limit?
print(sys.getrecursionlimit())
# we can also set it:
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())