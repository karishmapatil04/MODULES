# Python program for the above approach

# Function to find the minimum
# number of rabbits in the forest
def minNumberOfRabbits(answers, N):
    # initialize map
    Map = {}
    
    # Traverse array answers[] 
    # to the number of occurrences
    for a in range(N):
        if answers[a] in Map:
            Map[answers[a]] += 1
        else:
            Map[answers[a]] = 1
    
    # Initialize count
    count = 0
    
    # Find the rabbit groups and 
    # no. of rabbits in each group
    for a in Map:
        x = a
        y = Map[a]
        
        # Find number of groups and 
        # multiply them with number 
        # of rabbits in each group
        if (y % (x + 1)) == 0:
            count = count + ((y // (x + 1)) * (x + 1))
        else:
            count = count + ((y // (x + 1) + 1) * (x + 1))
    
    # count gives minimum number 
    # of rabbits in the forest
    return count

# Driver code
arr = [2, 2, 0, 0]
N = len(arr)

# Function Call
print(minNumberOfRabbits(arr, N))