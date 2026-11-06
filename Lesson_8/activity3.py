print("Hello! This program will help you select a ride.")

ride = int(input("\nEnter what category of ride you want (1 for bike, 2 for car): "))

if ride == 1:
    print("\nYou have chosen a bike.")
    biketype = int(input("\nWhat type of bike would you like (1 for sports, 2 for casual): "))
    if biketype == 1:
        print("\nYou have chosen a sports bike.")
    elif biketype == 2:
        print("\nYou have chosen a casual bike.")
    else:
        print("\nYour preferred bike type is not contained in our collection.")    
elif ride == 2:
    print("\nYou have chosen a car.")
    cartype = int(input("\nWhat type of car would you like (1 for sports, 2 for casual): "))
    if cartype == 1:
        print("\nYou have chosen a sports car.")
    elif cartype == 2:
        print("\nYou have chosen a casual car.")
    else:
        print("\nYour preferred car type is not contained in our collection")
else:
    print("\nYour input value is invalid for our selection standard.")              