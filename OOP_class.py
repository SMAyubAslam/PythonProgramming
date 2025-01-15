# Creating a Class:
# Let us now create a class using the class keyword.

# class Details:
#     name : "Ayub"
#     age : 28

# Creating an Object:
# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
# Example:

# obj1 = Details()

# Now we can print values:
# Example:

# class Details:
#     name = 'Ayub'
#     age = 28

# obj1 = Details()

# print(obj1.name)
# print(obj1.age)

# Self parameter:
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It must be provided as the extra parameter inside the method definition.
class Details:
    name = "Ayub"
    age = 28
    def description(self):
        print(f'My name is {self.name} and I am {self.age} years old.')

obj1 = Details()
obj1.description()