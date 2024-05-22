# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# Indexing
name = "Krenar Dervishaj"
first_name = name[:6] # Krenar start is exclusive and stop is inclusive, can be written as [0:6] as well
last_name = name[7:16] # Dervishaj start is inclusive and stop is exclusive, can be written as [7:] as well
step_name = name[0:8:3]
reversed_name = name[::-1] # jahsivreD raneK

print(first_name)
print(last_name)
print(step_name)
print(reversed_name)

# Slicing

website = "http://google.com"
slice = slice(7, -4) # 7 starts from http:// and -4 ends with .com so it will print google
print(website[slice])

website2 = "http://wikipedia.com"
print(website2[slice])