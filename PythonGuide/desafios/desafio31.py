'''

Crie uma função lambda que aceite um número e retorne "par" ou "ímpar"

'''

par_ou_impar = lambda x: 'par' if x % 2 == 0 else 'ímpar'

print(par_ou_impar(int(input('Digite um número: '))))