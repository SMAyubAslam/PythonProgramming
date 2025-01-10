'''
Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

Example 1:
'''
# tuple1 = (99,23,56,90,25,21)
# tuple2 = ("red","green","yellow","blue","black")
# print(tuple1)
# print(tuple2)

# detail = ('Ayub', 243, 27, "Automotive Software Engineering")
# print(detail)

'''
Accessing tuple items:
I. Positive Indexing:
As we have seen that tuple items have index, as such we can access items using these indexes.

Example
'''
# countries = ("Germany", "Nietherland", "France", "Switzerland")
# #               [0]         [1]            [2]      [3]
# print(countries[0])
# print(countries[1])
# print(countries[2])
# print(countries[3])

'''
II. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

Example:
'''
# countries = ("Germany", "Nietherland", "France", "Switzerland")
# #               [0]         [1]            [2]      [3]
# print(countries[-1])
# print(countries[-2])
# print(countries[-3])
# print(countries[-4])

'''
III. Check for item:
We can check if a given item is present in the tuple. This is done using the 'in' keyword.

Example 1:
'''
# food = ('biryani', 'pasta', 'burger', 'faluda')

# if 'burger' in food:
#     print('Burger is present')

# else:
#     print('Burger is not present')

'''
IV. Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

Syntax:
Tuple[start : end : jumpIndex]
Note: jump Index is optional. We will see this in given examples.

Example: Printing elements within a particular range:
'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[3:7])     #using positive indexes
# print(animals[-7:-2])   #using negative indexes
'''
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. Note: The element of the end index provided will not be included.

Example: Printing all element from a given index till the end
'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[4:])      #using positive indexes
# print(animals[-4:])     #using negative indexes
'''
When no end index is provided, the interpreter prints all the values till the end.

Example: printing all elements from start to a given index
'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[:6])      #using positive indexes
# print(animals[:-3])     #using negative indexes
'''
When no start index is provided, the interpreter prints all the values from start up to the end index provided.

Example: Print alternate values
'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[::2])     #using positive indexes
# print(animals[-8:-1:2]) #using negative indexes
'''
Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

Example: printing every 3rd consecutive withing given range
'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[1:8:3])
'''
Here, jump index is 3. Hence it prints every 3rd element within given index.
'''