def hello(first_name, last_name, age):
    print("Hello! " + first_name+" "+ last_name)
    print("You are " + str(age) + " years old")

hello("Renna", "Carneiro", 21)

#return statement

def multiply(number1, number2):
    return number1 * number2

Z = multiply(5,5)
print(Z)

#Keyword arguments

def hello(first,middle,last):
    print("Hello " + first + " " + middle + " " + last)
    
hello(last="Carneiro", first="Rennan", middle="Almeida")

#Nested functions calls
#num = input("Enter a number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input("Enter a number: ")))))

#args = parameter that will pack all arguments into a tuple useful so that a function can accept a varyind amount of arguments
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += 1
    return sum

print(add(1,2,3,4,5,6,7,8,9))

#kwargs = parameter that will pack all arguments into a dictionary. useful so that a function can accept a varying of keyword argum.
def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
        
hello(title = "MR. ", first = "Rennan", middle = "Almeida", last = "Carneiro")
