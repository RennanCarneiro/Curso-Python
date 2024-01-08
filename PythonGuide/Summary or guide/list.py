#list = used to store multiples items in a single variable

food = ["pizza", "sushi", "pasta", "pudding"]

#print(food[1])

food.append("Ice cream")
food.remove("pizza")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear() #remove todos os itens da lista

for i in food:
    print(i)