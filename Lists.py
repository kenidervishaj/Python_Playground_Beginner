# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi" # change the value of the first item in the list
food.append("ice cream") # add an item to the end of the list
food.remove("hamburger") # remove an item from the list
food.pop() # remove the last item from the list
food.insert(0, "cake") # add an item at a specific index
food.sort() # sort the list in alphabetical order

for x in food:
    print(x) # print each item in the list