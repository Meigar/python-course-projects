print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# TULIS BILL PER SIZE DULU
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you typed the wrong inputs.")

#
if pepperoni == "Y":
    if size == "S":
       bill += 2
    elif size == "M":
        bill += 3
else:
    bill += 0

# EXTRA CHEESE
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")