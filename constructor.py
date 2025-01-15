# Constructors
# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.
# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Types of Constructors in Python
# Parameterized Constructor
# Default Constructor

class Person():
    #def __init__(self):     #Default Constructor
        #print("Hi Good day Everyone")
    def __init__(self, name, acco):     #Parameterized Constructor
        self.name = name
        self.acco = acco
    def info(self):
        print(f"{self.name} is a {self.acco} in our company")

person1 = Person("Ayub","Software Developer")
person2 = Person("Amina","QA")
person1.info()
person2.info()
        