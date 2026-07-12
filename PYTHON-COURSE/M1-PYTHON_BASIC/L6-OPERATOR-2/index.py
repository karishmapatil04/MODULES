weather = "cloudy"
homework = "yes" 
day = "Saturday"


# Topic 5 - Combining AND + OR + NOT
if weather == "rainy" and not (homework == "yes"):
    print("Best plan : Stay in, finish homework first.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan : All set for a great school day!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan : Perfect weekend - head outside!")
else:
    print("Best plan : Take it one step at a time!")