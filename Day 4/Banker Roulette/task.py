import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# opsi 1 choice
print(random.choice(friends))

# opsi 2 sama saja randit
random_index = random.randint(0, 4)
print(friends[random_index])

