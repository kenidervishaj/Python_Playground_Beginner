# index operator [] = gives access to a sequence's element (string, list, tuple)

name = "Krenar Dervishaj"

if (name[1].islower()):
    name = name.capitalize()

print(name)
first_name = name[0:6].lower()
print(first_name)
last_name = name[7:].upper()
print(last_name)
last_character = name[-1].upper()
print(last_character)
