def list_length(arr):
    # Base case
    if arr == []:
        return 0
    
    # Recursive case
    return 1 + list_length(arr[1:])


# Given list
my_list = [10, 20, 30, 40, 50]

# Function call
print("Length of the list is:", list_length(my_list))