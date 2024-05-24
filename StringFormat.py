# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)

# Using str.format()

print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))

text = "The {} jumped over the {}"
print(text.format(animal, item))

# Using keyword arguments
print("The {a} jumped over the {i}".format(a=animal, i=item))
print("The {i} jumped over the {a}".format(a=animal, i=item))
