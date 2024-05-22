# set = collection which is unordered, unindexed. No duplicate values.

utensils = {"fork", "spoon", "knife", "plate", "glass", "cup", "bowl", "spoon"}
dishes = {"plate", "glass", "cup", "bowl", "spoon"}

utensils.add("napkin")  # adds an item to the set
utensils.remove("spoon")  # removes an item from the set
utensils.update(dishes)  # adds items from another set into the set

dinner_table = utensils.union(dishes)  # combines two sets into one set

for x in utensils:
    print(x)      # will not be in the same order as it was entered, and will not have duplicates


