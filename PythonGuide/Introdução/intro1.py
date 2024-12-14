# Comentários - com #

x = 2
print(x+80) 

x = str("7") # é string
y = int(4) # int
z = float(8) # float
w = str("oii") #string

print(x)
print(y)
print(z)

nome = "Rennan"
idade = 20
idade = str(idade) # transformando em String
cidade = "Rennan"
print('O ' + nome + " tem " + idade + " anos de idade e mora na cidade de " + cidade + '.')



# INPUT

'''
nome2 = input('Digite o seu nome: ')
idade2 =input('Digite a sua idade: ')
cidade2 = input('Digite sua cidade: ')


print('O ' + nome2 + " tem " + idade2 + " anos de idade e mora na cidade de " + cidade2 + '.')

'''

# SLICING

fruta = 'Abacate'
print(fruta[3]) # 0 - A / 1 - B / 2- A / 3 - C / 4 - A / 5 - T / 6 - E /

valor = 99.75
valor = str(valor)

print(valor[2:]) # pega o .75 pois conta 2 espaços.


# IMPRIMIR O Marcos Silva é um excelente [Programador]

nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'Programador'

print(texto)

texto2 = f'0 {nome} {sobrenome} é um excelente [{profissao}]'

print(texto2)
# MÉTODOS DE STRING

mensagem = 'Eu adoro programacao'

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.replace('adoro','amo')) # troca o "adoro" por "amo".
print(mensagem.capitalize()) # deixa em maiúsculo a primeira letra.
print(mensagem.find('a')) # procura em que local está a letra ou em que ponto começa uma palavra.
print(mensagem.find('adoro'))
print(mensagem.strip()) # remove qualquer espaço que tenha antes do primeiro caracter.