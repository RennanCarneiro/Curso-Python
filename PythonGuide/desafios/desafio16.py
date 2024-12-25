'''

Peça ao usuário que digite um número, se ele for maior que 10, imprima "o número é maior que 10",
se for menor, imprima "o número é menor que 10".

Bônus: diga se um número é impar ou par. (implementado por mim mesmo)

'''

numero = int(input("Digite um número: "))

if numero > 10:
    print("O número é maior que 10")
else:
    print("O número é menor que 10")
    
if numero % 2 == 0:
    print("O número é par")
else:  
    print("O número é ímpar")