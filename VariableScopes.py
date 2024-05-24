# scope = The region that a variable is recognized.
# A variable is only available from inside the region it is created. This is called scope.
# A global and locally scoped versions of a variable can be created.

def display_name():
    name = "Python" # local scope variable (only available inside the function)
    print(name)

name = "Java" # global scope variable (available everywhere)
print(name)