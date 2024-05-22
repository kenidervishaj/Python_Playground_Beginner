# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you? "))

if age == 100:
    print("How are you still alive?")
elif age >= 18: # if fullfilled, the code block will execute, and skip the rest of the code
    print("You are legal to drive a car!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are not legal to drive a car!")

