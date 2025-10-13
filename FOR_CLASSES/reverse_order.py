'''print("This program is only aplicable for single alphabet")
ch = input("Enter any alphabet: ")
if len(ch) == 1 and ch.isalpha():
    ascii_value = ord(ch)
    print("The ASCII code of", ch, "is:", ascii_value)
else:
    print("Please enter a single alphabet only!")'''

'''n = int(input("Enter a value of terms"))  
sum=0
i=0
while(i<=n):
    sum=sum+i
    i=i+1

print("sum=",sum)  '''

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")