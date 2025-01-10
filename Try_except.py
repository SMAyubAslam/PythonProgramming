'''
Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.
Example
'''
# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")

# a = input("Enter a number:")
# print(f"Multipliaction of {a} is")

# try:
#     for i in range(1,11):
#         print(f'{int(a)} X {i} =',int(a)*i)
# except:
#     print("Invalid input")

# print("Some imp lines of code")
# print("End of program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print('list index out of range')