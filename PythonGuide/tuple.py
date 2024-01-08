#tuple = collection wich is ordered and unchangeable used to group together related data

student = ("Ren", 21, "male")

print(student.count("Ren"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Ren" in student:
    print("He is here!")