name = input("Enter your name: ")
age = input("Enter your age: ")
#se quiser incrementar age + 1 terá q transformar em integer primeiro.
# age = int(input("Enter your age: "))

print(f"Hello {name}", f", you are {age} years old")

#Ex: complete the sentence
print("Chose an adjective to complete the sentence below.")
adjective = input("Enter an adjective: ")
print(f"Today i went to a {adjective} restaurant.")

print("Chose a noun to complete the sentence below.")
noun = input("Enter a noun: ")
print("At the cinema, I met {noun}")

#Ex 2: area calculate
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the wifth of a rectangle: "))

area = length * width

print(f"The area is: {area}cm^2")



