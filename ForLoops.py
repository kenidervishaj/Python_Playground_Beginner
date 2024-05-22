import time

# for loop = a statement that will execute its block of code a limited amount of times
# while loop = unlimited
# for loop = limited

# for i in range(10): # range(10) = 0 to 9
    # print(i+1)

# for i in range(50, 100, 10): # range(50, 100) = 50 to 99
#     print(i)

# for i in "Krenar Dervishaj":
#     print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1) # will wait 1 second before each print statement

print("Happy New Year!")