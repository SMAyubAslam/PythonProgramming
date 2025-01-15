# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# Here is an example of how to use a lambda function:
# def double(x):     #Function to double the input
#     return x*2
# print(double(2))

# double = lambda x : x*2      #lamda Function to double the input
# print(double(2))

# Lambda functions can also include multiple statements, but they are limited to a single expression. For example:

# Lambda function to calculate the product of two numbers,
# with additional print statement
# lambda x, y: print(f'{x} * {y} = {x * y}')

# we can use func into func
def fun1(fun2 , value):
    return 6 + fun2(value)

print(fun1(lambda x : x * x, 2))