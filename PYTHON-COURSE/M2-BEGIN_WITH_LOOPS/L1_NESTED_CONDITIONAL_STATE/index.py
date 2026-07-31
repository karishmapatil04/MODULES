choice=int(input("Enter the choice of ride:"))

if choice == 1:    
    bike_type=int(input("Enter bike choice:"))         
    # outer: Bike
    if bike_type == 1:
        print("Scooty — 80 km/h")
    else:
        print("Mountain Bike — 40 km/h")
elif choice == 2:   
    car_type=int(input("Enter car choice:"))
        # outer: Car
    if car_type == 1:
        print("Sedan — 5 seats")
    else:
        print("SUV — 7 seats")
else:
    print("Invalid choice")

