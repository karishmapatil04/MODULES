import datetime
import calendar

now123 = datetime.datetime.now()
print("Time now:", now123)

print(calendar.calendar(now123.year))