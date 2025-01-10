'''
Python Dictionaries
Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# print(info)

'''
Accessing Dictionary items:
I. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# print(info['Name'])
# print(info.get('Name'))

'''
II. Accessing multiple values:
We can print all the values in the dictionary using values() method.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# print(info.values())

'''
III. Accessing keys:
We can print all the keys in the dictionary using keys() method.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# print(info.keys())

'''
IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# print(info.items())

# for key, value in info.items():
#     print(f'The value corresponding to the key {key} is {value}')
#-----------------------------------Dictionary Method----------------------------------#
'''
update()
The update() method updates the value of the key provided to it if the item already exists in the dictionary, 
else it creates a new key-value pair.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# info.update({'Age':28})
# info.update({'DOB':'21/11/1996'})
# print(info)
'''
There are a few methods that we can use to remove items from dictionary.

clear():
The clear() method removes all the items from the list.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# info.clear()
# print(info)
'''
The pop() method removes the key-value pair whose key is passed as a parameter.

Example:
'''
# info = {'Name':'Ayub', 'Age':27, 'City':'Frankfurt'}
# info.pop('Name')
# print(info)
'''
popitem():
The popitem() method removes the last key-value pair from the dictionary.

Example:
'''
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# info.popitem()
# print(info)
'''
del:
we can also use the del keyword to remove a dictionary item.

Example:
'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
'''
If key is not provided, then the del keyword will delete the dictionary entirely.

Example:
'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)