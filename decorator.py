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

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b