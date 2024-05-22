# tuple = collection of items which is ordered and unchangeable
#         used to group together related data

student = ("Krenar", 21, "Male")

print(student.count("Krenar"))
print(student.index("Krenar"))

print("The name of the student is: " + student[0])
print("The age of the student is: " + str(student[1]))
print("The gender of the student is: " + student[2])

for x in student:
    print(x)

if "Krenar" in student:
    print("Yes, 'Krenar' is in the student tuple")
else:
    print("No, 'Krenar' is not in the student tuple")