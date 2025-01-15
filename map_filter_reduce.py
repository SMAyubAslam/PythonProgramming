# def cube(x):
#     return x*x*x

# l = [1, 3, 5, 8, 10]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

# MAP func
# def cube(x):
#     return x*x*x
# l = [1, 3, 5, 8, 10]
# newl = list(map(cube, l))   #map(cube, l) will return map object so we have to typecast it to our desire data type for example List here.
# print(newl)

# Map, Filter and Reduce
# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

# map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the map function:

# numbers = [2, 4, 6, 8, 10]

# double = map(lambda x: x*x, numbers)    # Double each number using the map function
# print(list(double))

# FILTER func
# def filter_func(a):
#     return a>2
# l = [1, 3, 5, 8, 10]
# newl = filter(filter_func,l)
# print(list(newl))

# filter(predicate, iterable)

# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the filter function:
# l = [1, 3, 5, 8, 10]
# newl = filter(lambda x: x%2 == 0, l)
# print(list(newl))

#REDUCE func
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:
# reduce(function, iterable)
from functools import reduce

l = [1, 3, 5, 8, 10]
newl = reduce(lambda x, y: x + y, l)
print(newl)

# In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements in the numbers list. The lambda function adds the two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3), and so on. The final result is the sum of all the elements in the list, which is 15.
# It is important to note that the reduce function requires the functools module to be imported in order to use it.


