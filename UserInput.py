name = input("Enter your name: ")

print("Hello, " + name)

age = input("Enter your age: ")
age = int(age) + 1 # Convert age to integer and add 1
print("You are " + str(age) + " years old.") # Convert age back to string

height = input("How tall are you in meters? ")
height = float(height)
print("You are " + str(height) + " meters tall.")
