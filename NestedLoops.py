# nested loops = a loop inside of a loop
#                The inner loop will finish all of its iterations
#                before the outer loop finishes one.

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # end="" will print the next symbol on the same line as the previous one
    print() # This will move the cursor to the next line after the inner loop finishes