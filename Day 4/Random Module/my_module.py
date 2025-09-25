import random
#
# random_integer = random.randint(0, 10)
# print(random_integer)

# KALAU RANDOM 0 KOMA
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

#  KALAU RANDOM 0 KOMA DI KALI 10 (LEBIH REKOMENDASI DARIPADA UNIFORM
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)


random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")