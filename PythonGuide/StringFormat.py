animal = input("Enter an animal: ")
item = input("Enter an item")

#print("The {} jumped over the {}".format(animal, item)) #{0},{1}. {1},{0}. {animal},{item}.
text = "The {} jumped over the {}"
print(text.format(animal, item))

###########################################
name = "Rennan"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))

##############################################
number = 3.14159
print("Pi is {:.2f}".format(number))
print("Pi is {:,}".format(number))
print("Pi is {:b}".format(number))
print("Pi is {:o}".format(number))
print("Pi is {:X}".format(number))
print("Pi is {:E}".format(number))