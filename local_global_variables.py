# A local variable is a variable that is defined within a function and is only accessible within that function. 
# It is created when the function is called and is destroyed when the function returns.

# On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any 
# function in your code.

# Here's an example to help clarify the difference:

# x = 10  #global variable

# def my_function():
#     y = 5   #local variable

# my_function()
# print(x)
# print(y)    #this will cause an error because y is a local variable and is not accessible outside of the function

# The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope. 
# Here's an example:

# x = 25

# def my_fun():
#     global x
#     x = 9
#     y = 3
# my_fun()
# print(x)
# print(y)    #this will cause an error because y is a local variable and is not accessible outside of the function

# In this example, we used the global keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is changed to 5.

# It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.

# I hope this tutorial has helped clarify the differences between local and global variables and how to use the global keyword in Python. Thank you for watching!