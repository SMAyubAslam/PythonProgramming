a = [1, 2, 4] #list are mutable so memory location would be different
b = [1, 2, 4]

print(a is b)   # exact location of object in memory    #False
print(a == b)   # value     #True


# One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result:

a = 3 #Integers are immutable so memory location would be same
b = 3

print(a is b)   # exact location of object in memory    #True
print(a == b)   # value     #True

# In these cases, a and b are both pointing to the same object in memory, so is and == both return True.
# For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same object in memory.