# Taking total amount as input from user
Amount =int(input("Please Enter Amount for Withdraw :"))

# Calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10


print( "notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)


#pgm for calculating total number of years,weeks and days
print("Enter the Number of Days: ")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("Total Number of Year(s): ")
print(year)
print("Total Number of Week(s):")
print(week)
print("Total Number of Day(s):")
print(days)