def factorial(x):
  if x==0 or x==1:
      return 1
  else:
    #calling function inside a function
      return x*factorial(x)

#display result
print("the factorial of 0:",factorial(4))
