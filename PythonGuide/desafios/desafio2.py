'''

Declare duas variáveis: uma chamada 'nome', que deve guardar o seu primeiro nome como String,
e outra chamada 'idade', que deve guardar sua idade como um número inteiro.
Depois disso, imprima na tela uma frase que diga "Olá, meu nome é [nome] e eu tenho [idade] anos.

'''

def declarar():
    nome = input("Insira seu nome: ")
    idade = int(input("Insira sua idade: "))
    print(f"Olá, meu nome é {nome} e tenho {idade} anos")