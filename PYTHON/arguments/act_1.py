''''num = 29
flag = False

# check for factors
for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")'''

def total_cal(bill_amount, tip_perc):
    total= bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print("total pay",total)

total_cal(150,20)    
