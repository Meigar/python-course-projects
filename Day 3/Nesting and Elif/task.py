print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
#
# IF ELSE SAJA
# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")



# PAKE ELIF (ELSE IF) KALAU LEBIH DARI SATU. ELIF BISA LEBIH DARI SATU TAPI IF SAMA ELSE CUMA 1 SAJA.
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age <= 12:
        print("please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")

        # SOAL EXERCISE DAR 3 NO 24 IT WORKS!
        # weight = 85
        # height = 1.85
        #
        # bmi = weight / (height ** 2)
        #
        # # 🚨 Do not modify the values above
        # # Write your code below 👇
        #
        # print("check your BMI")
        # BMI = int(input("What is your BMI? "))
        #
        # if height <= 18.5:
        #     print("you are underweight 85")
        # elif height >=18.5-25:
        #     print("you have normal weight 85")
        # else:
        #     print("you have overweight")