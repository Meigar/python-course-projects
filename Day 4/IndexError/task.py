# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# print(states_of_america)
#
#  LIST BISA DIGABUNGKAN
# fruits = ["Cherry", "Apple", "Pear"]
# vegetables = ["Cucumber", "Kale", "Spinnach"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
#
# # QUIZ
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0]) #kurung pertama saja karena SEMUA MULAI DARI 0
print(dirty_dozen[1]) #kurung kedua saja
print(dirty_dozen[1][2]) #kurung kedua nomor kedua yaitu tomat
print(dirty_dozen[1][3]) #kurung kedua nomor tiga itu celery
print(dirty_dozen[1][1]) #kurung kedua nomor kedua yaitu kale. jadi strawberry dan spinach sama sama nomor 0