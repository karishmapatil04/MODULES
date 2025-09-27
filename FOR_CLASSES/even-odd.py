'''number=int(input("Enter a number to check even odd:"))
if(number%2 == 0):
    print("The number is even")
else: 
    print("The number is odd")   ''' 

actual_cost=float(input("Enter actual price of object"))
sell_cost=float(input("Enter the selling cost of object"))
amount=sell_cost-actual_cost
if(sell_cost>actual_cost):
    print("You have gained profit", amount)
else:
    print("no profit")    

