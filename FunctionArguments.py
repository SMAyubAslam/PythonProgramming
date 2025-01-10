'''
Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

Example:
'''
# def name(fname, mname = "Bread", lname = "Shawn"):
#     print("My name is",fname,mname,lname)

# name("Jhon")

'''
Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

Example:
'''
# def average(a,b,c):
#     print("The average of given numbers is",(a+b+c)/3)

# average(a=3,b=2,c=4)

'''
Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

Example:
'''
# def name(fname, mname, lname):
#     print("My name is",fname,mname,lname)

# name("Jhon","Bread","Shawn")
'''
Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Example:
'''
# def name(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#         print("Average is",sum / len(numbers))

# name(3,6,9)
'''
Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

Example:
'''
# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])
# name(mname = "Buchanan", lname = "Barnes", fname = "James")
'''
return Statement
The return statement is used to return the value of the expression back to the calling function.

Example:
'''
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))
