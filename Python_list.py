'''
Accessing list items
We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

Positive Indexing:
As we have seen that list items have index, as such we can access items using these indexes.

Example:
'''
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])
'''
Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

Example:
'''
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]    #Tips when you get negative index convert it into positive by len of list 
# #          [-5]    [-4]    [-3]     [-2]      [-1]      # - negative index 
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

'''
Check whether an item in present in the list?
We can check if a given item is present in the list. This is done using the in keyword.
'''
# fruit = ["Mango", "Banana", "Lichi", "Orange"]
# if "Orange" in fruit:
#     print(True)
# else:
#     print(False)

'''
Range of Index:
You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

Syntax:

listName[start : end : jumpIndex]
Note: jump Index is optional. We will see this in later examples.

Example: printing elements within a particular range:
'''
# animal = ["Lion", "Tiger", "leoperd", "Bull", "Elephant", "Donkey", "Pig", "Deer"]
# print(animal[2:5])
# print(animal[-7:-3])    #8-7 = [1]=Tiger, 8-3 = [5]=Donkey Output will be []"Tiger", "leoperd", "Bull", "Elephant"]
# print(animal[4:])    
# print(animal[-4:])    #8-4 = [4]=Elephant -> ["Elephant", "Donkey", "Pig", "Deer"]]
# print(animal[1:8:2])    

'''
List Comprehension
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

Syntax:
List = [Expression(item) for item in iterable if Condition]

Expression: It is the item which is being iterated.

Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.

Example 1: Accepts items with the small letter “o” in the new list
'''
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
