'''
Raising Custom errors
In python, we can raise custom errors by using the raise keyword.
'''
# salary = int(input('Enter Salary Amount : '))
# if not 2000 < salary < 5000:
#     raise ValueError('Not a valid salary')

a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 