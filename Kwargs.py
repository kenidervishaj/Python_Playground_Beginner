# **kwargs = parameter that will pack all arguments into a dictionary
# Useful so that a function can accept a varying amount of keyword arguments

def hello(**names):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'] + " " + kwargs['middle'])
    print("Hello ", end = "")
    for key,value in names.items():
        print(value)

hello(first = "Corey", last = "Schafer", middle = "M.S.")