'''

Crie uma função lambda que aceite um número e retorne o cubo deste número.

Bônus: soma.

'''

x = input('Digite um número: ')
cubo = lambda x: x ** 3
print(cubo(int(x)))