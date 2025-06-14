#geraldworks  
print("\nWelcome to the RollerCoaster!")
print("Tickets: Age 7-11 years($5) | Age 12-18 years($7) | Age 19-45 years($12) \nHeight should be up to 120cm! | Additional Photos($3)")
height = int(input("\nWhat is your height in cm? "))
age = int(input("What your age? "))
bill = 0

if height >= 120:
    print("\nYou can ride a rollercoaster!")

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")



else:
    print("Sorry, you have to grow taller before you can ride.")
      