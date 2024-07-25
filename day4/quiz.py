import random
names = ["Angela", "Ben", "Jenny", "Michael", "chloe"]

num_items = len(names)

random_choice = random.randint(0, num_items -1)
print(f"{names[random_choice]} is going to buy the meal today!")


#to find the position of angela in the list
#print(names.index("Angela"))