'''

As funções recursivas são funções que se chamam dentro do seu próprio bloco de código. Elas são
úteis para resolver problemas que podem ser divididos em problemas menores de natureza semelhante.

Um exemplo clássico de onde a recursão é usada é o cálculo do fatorial de um número. O fatorial de um
número n é o produto de todos os números inteiros positivos de n até 1.

'''

import math

def fatorial(n): # Função que calcula o fatorial de um número
    if n == 0: # Caso base da recursão (fatorial de 0 é 1)
        return 1 # Caso base da recursão (fatorial de 0 é 1)
    else: # Caso geral da recursão
        return math.factorial(n) # Chamada recursiva

x = int(input('Digite um número: ')) # Solicita um número ao usuário
print(fatorial(x)) # Imprime o fatorial do número digitado
