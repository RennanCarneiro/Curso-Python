import random
#guess the number
x = random.randint(1,5)

y = random.random() #random float

myList = ['Rock', 'Paper', 'Scisssors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards)