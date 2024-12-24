'''
criar um programa que dependendo da temperatura da carne ele irá retornar o ponto de cozimento.
O usuario deverá fornecer a temperatura
'''
temperatura = input("Insira a temperatura da carne: ")

if temperatura < 48:
    print("Raw")
elif temperatura >= 48 and temperatura < 54:
    print("Rare")
elif temperatura >= 54 and temperatura < 60:
    print("Medium rare")
elif temperatura >= 60 and temperatura < 65:
    print("Medium")
elif temperatura >= 65 and temperatura < 71:
    print("Medium well")
elif temperatura == 71:
    print("Well done")
else:
    print("Burnt meat")

    