#Create a python program capable of greeting you with Good Morning, 
# Good Afternoon and Good Evening. 
# Your program should use time module to get the current hour. 
# Here is a sample program and documentation link for you:

'''
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59
'''

import time
nm = "Ayub"
recentTime = time.strftime('%H:%M:%S')
RecentTime = int(time.strftime('%H'))

if (4<= RecentTime <12):
    print("Good Morning",nm, "it's",recentTime)

elif (12<= RecentTime <17):
    print("Good Afternoon",nm, "it's",recentTime)

elif (17<= RecentTime <21):
    print("Good Evening",nm, "it's",recentTime)

else:
    print("Good Night",nm, "it's",recentTime)
