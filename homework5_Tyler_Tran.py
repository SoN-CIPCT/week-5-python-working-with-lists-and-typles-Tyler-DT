# 1 Create a list that contains 6 items.
mylist = ["corgi", "shiba", "pomeranian", "samoyed", "husky", "akita"]

# 2 Print the items in the list to the output console.
print("The items in the list are:", mylist)

# 3 Print the first two items using a slice
print(f"The first two items in the list are: {mylist[0:2]}")

# 4 Print the middle two items using a slice
print(f"The middle two items in the list are: {mylist[2:4]}")

# 5 Print the first and last items using indexes
print(f"The first and last items in the list are: {mylist[0]}, {mylist[-1]}")

# Tuple Exercises
# 1 Decide on  five foods and store them in a tuple
menu = ("apple", "banana", "cucumber", "date", "elderberry")

# 2 Print each item on the menu using a for loop
print("Original menu:")
for fruit in menu:
    print(fruit)

#  3 Copy the tuple replacing two of the foods on the menu
updated_menu = ("apple", "baobab", "calamansi", "date", "elderberry")

#  4 Print each item on the revised menu using a loop
print("Updated menu:")
for fruit in updated_menu:
    print(fruit)
