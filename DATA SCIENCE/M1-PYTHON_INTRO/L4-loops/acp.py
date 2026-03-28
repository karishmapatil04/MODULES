# Taking input from user
num = int(input("Enter a number: "))

# Store original number
original_num = num

# Count number of digits
num_digits = len(str(num))

# Calculate Armstrong sum
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

# Check result
if sum == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is NOT an Armstrong number")