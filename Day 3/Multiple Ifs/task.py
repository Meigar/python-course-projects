print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("adult tickets are $12.")

    wants_photo = input("do you want to have take the pics? type y for yes and n for no.")
    if wants_photo == "y":
    # add photo for $3
        bill += 3
    print(f"your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")

