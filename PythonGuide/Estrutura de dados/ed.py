from sys import getsizeof

# Função Lambda
# É uma função pequena e sem nome, podendo ter vários argumentos, mas somente uma expressão.
# É muito utilizada dentro de outras funções, e deixa o código mais limpo.

def somar(x):
    return x + 10

print(f'Função somar - {somar(2)}')

# argumento: x | lambda: x+10

somar10 = lambda x: x + 10
print(f'Modo Lambda - {somar10(2)}')

somar2N = lambda x, y: x + y + 10
print(somar2N(2, 4))  # 16

# Lambda dentro de uma função

def somar(x):
    funcao2 = lambda x: x + 10
    return funcao2(x) * 4

print(somar(2))

# Função Map em uma Lista
# Muito utilizado em listas, e aplica uma função a um iterable, por item. (list, tuple, dicionário, etc.)
# Criar um programa que multiplica os valores da lista [1,2,3,4] por 2
# Resultado desejado = [2,4,6,8]

lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

lista2 = map(multi, lista1)
print(list(lista2))  # --> [2,4,6,8]

# Função Map com lambda
# Criar um programa que transforme estas 6 linhas de código em apenas uma

print(list(map(lambda x: x * 2, lista1)))

# Função Filter
# Criar um programa que filtre valores abaixo de 20

valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))  # Com função
print(list(filter(lambda x: x > 20, valores)))  # Com lambda

# List Comprehension com String
# Forma mais fácil de escrever, utilizado quando você precisa criar uma nova lista a partir de outra existente.
# [expressão for item in itens]
# Fazer um programa que jogue em outra lista as frutas que contém a letra "B"

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []  # lista vazia
frutas3 = []  # lista vazia

for letras in frutas1:
    if 'b' in letras:
        frutas2.append(letras)  # Adiciona as frutas com 'b' na lista 2
    else:
        frutas3.append(letras)  # Adiciona as frutas sem 'b' na lista 3

print(frutas1)
print(frutas2)
print(frutas3)
print()

# Agora, tudo isto novamente em apenas 1 linha de código:
frutas4 = [letra for letra in frutas1 if 'b' in letra]
print(frutas4)

# List Comprehension com Números
# Fazer um programa que some 10 em 10 a cada index.

numeros = []
for x in range(6):
    numeros.append(x * 10)

print(numeros)

# Agora, tudo isto em apenas uma linha de código:
novaLista = [x * 10 for x in range(6)]
print(novaLista)

# Lista e Generator Expressions
# Uma forma mais rápida para listas, dicionários e etc.
# Menos memória alocada.
# Valores em bytes.
# Para usar, só trocar os colchetes pelos parênteses.

numeros2 = [x * 10 for x in range(50)]
numeros3 = (x * 10 for x in range(50))

print(list(numeros2))
print(getsizeof(numeros2))  # 472 bytes com a lista.

print(list(numeros3))
print(getsizeof(numeros3))  # 200 bytes com o generator.
