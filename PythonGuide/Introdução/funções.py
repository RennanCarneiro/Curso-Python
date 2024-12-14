import math


#Funções - Início

def boas_vindas():
    print('Olá')
    print('Bom Dia')

boas_vindas() 

print('----- Aula 41 -----')
#Variáveis dentro da Função
def soma():
    n1 = 10
    n2 = 20
    resultado = n1 + n2
    print(resultado)


soma()


#Funções com parâmetros e argumentos

def boas_vindas(nome,quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} cadernos em estoque')

boas_vindas('Joao',5)
boas_vindas('Marcos',4)
boas_vindas('Sergios',3)


    #Argumentos Default e Non - Default
    # Default - Aquele que você define o valor no parâmetro
    # Non - Default - Aquele que você não define o valor no parâmetro

def bem_vindo(nome,quantidade=6): # nome = non-default | quantidade = default. O default deve estar sempre em último
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} cadernos em estoque')


bem_vindo('Chico') # Printa o Chico que eu passei, e que tem 6 cadernos, pois é o default da função.
print()


#Print e Return em Funções

def cliente1(nome):
    print(f'Olá {nome}')

cliente1('Maria')

def cliente2(nome):
    return f'Olá {nome}'

print(cliente2('Cristian'))


#Argumentos - XArgs - Criar uma função que soma vários números

def somar(*numeros): # Quando põe o asterisco, significa que vários números podem entrar na função, e não há um definido. (def soma já existe na Aula 41).
    resultado = 0 # ponto de início
    for num in numeros:
        resultado += num
    return resultado

x = somar(2,3,4,7)
print(x)


#Vários argumentos xargs nomeando argumentos - Criar uma função que armazena números e strings

def agencia(**carro): # dois asteriscos significam que você pode passar os parâmetros embaixo
    return carro

print(agencia(marca = 'Gol', cor = 'Branco', motor = 1.0, placa = 1234))
print(agencia(marca = 'Gol', cor = 'Preto', motor = 1.0))
print(agencia(marca = 'Gol', cor = 'Azul'))


#Importando um Módulo
# Qual o fatorial de quatro? R = 4 * 3 * 2 *1 = 24

fatorial = 4*3*2*1
print(f'Calculado manualmente - {fatorial}')

# Agora, qual o fatorial de 10? Como é longo, podemos usar a biblioteca "Math"
# Deve-se importar o módulo math (checar na linha 1)

print(f'Calculado com a biblioteca math - {math.factorial(4)}')
print(f'Fatorial de 10 com a biblioteca math - {math.factorial(10)}')

print(math.floor(2.7)) # arredonda pra baixo.
print(math.ceil(2.7)) # arredonda pra cima.