'''
Python Sets
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

Example:
'''
# s = {'Ayub', 27, 243, 'Automotive'}
# print(s)

'''
Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set
'''
# ayub = set()
# print(type(ayub))

'''
Accessing set items:
Using a For loop
You can access items of set using a for loop.

Example:
'''
s = {'Ayub', 27, 243, 'Automotive'}
for item in s:
    print(item)