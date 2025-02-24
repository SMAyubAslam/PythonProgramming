# Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

# In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.


# def greet(fx):
#     def mfx():
#         print("Good Mornig")
#         fx()
#         print("Hope we will see you again")
#     return mfx

# @greet
# def hello():
#     print("Hello every i hope you all are doing well")

# hello()

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Mornig")
#         fx(*args, **kwargs)
#         print("Hope we will see you again")
#     return mfx

# @greet
# def add(a,b):
#     print(a+b)

# add(2,4)

