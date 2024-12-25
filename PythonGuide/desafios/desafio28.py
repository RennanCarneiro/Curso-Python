'''

Crie duas funções. A primeira deve aceitar um número e retornar o dobro desse número.
A segunda deve aceitar um número e retornar o quadrado esse número. Em seguida, chame a
primeira função dentro da segunda para retornar o quadrado do dobro de um número.

'''

def dobro(n):
    return n * 2

def quadrado(n):
    return dobro(n) ** 2

n = int(input('Digite um número: '))
print(quadrado(n))