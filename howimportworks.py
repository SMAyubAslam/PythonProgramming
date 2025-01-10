# import math

# result = math.sqrt(9)
# print(result)

# (2)"from keyword"
# You can also import specific functions or variables from a module using the from keyword. For example, 
# to import only the sqrt function from the math module, you would write:

# from math import sqrt

# result = sqrt(9)
# print(result)


# (3) "You can also import multiple functions or variables at once by separating them with a comma:""

# from math import sqrt,pi

# result = sqrt(9)
# print(result)
# print(pi)

#(4) "Importing everyyhings using •"

# from math import *

# print(sqrt(9))
# print(pi)

#(5) "The "as" keyword"

# import math as m

# print(m.sqrt(9))
# print(m.pi)

# (6)"The dir function"
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables 
# defined in a module. This can be helpful for exploring and understanding the contents of a new module.

import math

print(dir(math))

