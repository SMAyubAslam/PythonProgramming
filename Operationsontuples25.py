'''
Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

Example:
'''
# countries = ("Germany", "USA", "England", "Canada", "Irland")
# temp = list(countries)
# temp.append("Austrailia")      #add on tuple
# temp.pop(4)
# temp[0] = "Newzeland"

# countries = tuple(temp)
# print(countries)
'''
Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

However, we can directly concatenate two tuples without converting them to list.

Example:
'''
# countries1 = ('Pakistan', 'Bangladesh', 'China', 'Afganistan')
# cpountries2 = ('India', 'Srilanka', 'Nepal', 'Korea')

# print(countries1 + cpountries2)
'''
Tuple methods
As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

count() Method
The count() method of Tuple returns the number of times the given element appears in the tuple.

Syntax:
tuple.count(element)
'''
# numbers = (4, 5, 4, 6, 2, 8, 9, 3, 3, 5, 10)
# res = numbers.count(6)
# print('Count of 6 is',res)

'''
index() method
The Index() method returns the first occurrence of the given element from the tuple.

Syntax:
tuple.index(element, start, end)
Note: This method raises a ValueError if the element is not found in the tuple.

Example
'''
# num = (2, 1, 2, 4, 2, 9, 8, 3, 7)
# res = num.index(4)
# print(res)