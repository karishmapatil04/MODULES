''''num = int(input("Enter a number to check for even or odd"))

if num%2 == 0:
    print("The number is even")
else:
    print("The number is odd")    '''


import datetime  
    
# using now() to get current time  
current_time = datetime.datetime.now()  
    
# Printing value of now.  
print("Time now at greenwich meridian is : ", end = "")   
print(current_time)

# print calendar of year 2021
import calendar
print("\n", calendar.calendar(2025))
