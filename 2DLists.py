# 2D lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0][1]) # will print the 2 element of the first list
print(food[1][2]) # will print the 3 element of the second list
# print(food[2][2]) # will not print the 3 element of the third list, since there is no 3 element in the third list