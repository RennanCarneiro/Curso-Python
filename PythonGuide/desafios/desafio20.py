'''

Crie uma lista de números de 1 a 10. Use um "for" para iterar sobre a lista. Se o número atual
da iteração for par, imprima "O número [número] é par.". Se for ímpar, imprima "O número [número] é ímpar."

'''

numeros = list(range(1, 11)) # cria uma lista de números de 1 a 10

for i in numeros:
    if i % 2 == 0: # se o número atual da iteração for par
        print(f"O número {i} é par.")
    else: # se o número atual da iteração for ímpar
        print(f"O número {i} é ímpar.")