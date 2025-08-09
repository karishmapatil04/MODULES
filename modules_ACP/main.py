"""x=17
y=25

if(x>y):
 print("x is greater then y")
else:
 print("y is greater then x")"""

costprice =int(input("enter the cp: "))
sellingprice =int(input("enter the sp: "))

if(sellingprice>costprice):
  print("profit")
  pt=sellingprice-costprice
  print(pt)
else :
  print("No profit")