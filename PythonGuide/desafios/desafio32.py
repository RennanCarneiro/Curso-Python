'''

Crie uma função lambda que eleve um número ao quadrado. Em seguida, use essa função para
calcular o quadrado de todos os números em uma lista usando um "for".

'''

quadrado = lambda x: x ** 2

numeros = list(range(1, 11))

for numero in numeros:
    print(quadrado(numero)) # 1, 4, 9, 16, 25, 36, 49, 64, 81, 100