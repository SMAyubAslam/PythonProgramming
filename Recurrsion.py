'''
Recursion in python
Recursion is the process of defining something in terms of itself.

Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

Example:
'''
# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# Quick Quiz: Write a program to print the Fibonacci sequence

# def febonacci(n):
#     if (n == 0):
#         return 0
#     elif (n == 1):
#         return 1
#     else:
#         return febonacci(n-1)+febonacci(n-2)

# print(febonacci(6))

a = int(input("Enter any number : "))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(a):
    print(fibonacci(i))