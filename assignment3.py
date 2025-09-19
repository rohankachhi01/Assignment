# Task 1: Calculate Factorial Using a Function?

def factorial(n):
    if n == 0 or  n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number you number : "))
result = factorial(n)
print("TASK1 the factorial of", n, "is", result)


# Task 2: Using the Math Module for Calculations?
a = int(input("enter the number :  "))
from math import sqrt
from math import log
from math import sin
print("TASK2 the square root of", a, "is", sqrt(a))
print("TASK2 the log10 of", a, "is", log(a))
print("TASK2 the sine of", a, "is", sin(a))

