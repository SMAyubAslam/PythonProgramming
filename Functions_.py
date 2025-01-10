def CalculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

a = 34
b = 44
isGreater(a,b)
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")

CalculateGmean(a,b)

c = 32
d = 23
isGreater(c,d)
# if(c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")

CalculateGmean(c,d)