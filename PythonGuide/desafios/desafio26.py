'''

Crie uma função que calcule a potência de um número. A função deve aceitar dois argumentos:
a base e o expoente. No entando, se o expoente não for fornecido ao chamar a função, ele deve assumir
o valor padrão de 2.

'''

def potencia(base, expoente):
    if expoente == 0:
        expoente = 2
    return base ** expoente

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
print(potencia(base, expoente))