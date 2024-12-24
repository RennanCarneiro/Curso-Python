'''

Utilize um while para imprimir os números de 1 a 10

'''
i = int(input("Digite a quantidade: "))

def contar(i):
    x = 1
    while x <= i:
        print(x)
        x += 1
        
contar(i)