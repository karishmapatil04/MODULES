# Program to find the amount of water that we can trap within a given set of bars.
 
def findWater(a, a_size):
 
    # Make array to hold the height of left tallest bar for any ith bar
    leftTallest = [0]*a_size
 
    # Make array to hold the height of the right tallest bar for any ith bar
    rightTallest = [0]*a_size
 
    # Initialize result
    water = 0
 
    # Fill left array
    leftTallest[0] = a[0]
    for i in range( 1, a_size):
        leftTallest[i] = max(leftTallest[i-1], a[i])
 
    # Fill right array
    rightTallest[a_size-1] = a[a_size-1]
    for i in range(a_size-2, -1, -1):
        rightTallest[i] = max(rightTallest[i + 1], a[i])
 
    # Water trapped for any ith bar should be minimun of the left and right highest bar - bar height
    for i in range(0, a_size):
        water += min(leftTallest[i], rightTallest[i]) - a[i]
 
    return water
 
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
bars = len(a)
print("Water : ", findWater(a, bars))
 
