import random #importing module
import time 
import calendar

def getRandomDate(startDate, endDate ): #defining function
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
#display result
print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))


#print("display calender",calendar.month(2025,12))