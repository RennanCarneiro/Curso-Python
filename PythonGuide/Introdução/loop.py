# For Loops

#imprimir de 1 a 5 

for numero in range (5+1):
    print(numero)

print("---------")

for numero in range(1,2):
    print(numero)
    
print("---------")

for letra in 'Google':
    print(letra)

print("---------")

palavra = 'Paito'

for letra in palavra:
    print(letra + ' forma a palavra paito')

print("---------")

palavra2 = 'Espetacular'

for letra in palavra2: 
    print(f'{letra} forma a palavra espetacular formatada')
print("---------")


# Enviar um email com os detalhes da compra online (Max 3 tentativas) para compras confirmadas.

compra_confirmada = False
dados_compra = 'Compra no valor de R$ 12.50 e entrega confirmada'


for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
else:
    print('Falha na compra.')
    
print("---------")
# Nested Loops

for numero1 in range(1,6):
    print('Produto ' + str(numero1))
    for numero2 in range(11):
        print(numero1,numero2)

print("---------")

# Modificar Fantastico para F A N T A S T I C O

palavra = 'FANTASTICO'
for espaco in palavra:
    print(f'{espaco}' , end= " ")
    

''' Criar um retangulo de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linhas = 6
colunas = 6
simbolo = '@'
print("---------")

for l in range (linhas):
    for c in range(colunas):
        print(simbolo,end = ' ')
    print()
    
#Programa em que um produto cai 5 reais por dia, até 20. Se acabar o estoque antes, encerra o programa.
print('----- Aula 36 -----')
valor = 100
dia = 0
while valor > 20:
    print(f' dia {dia+1} = R$ {valor},00')
    dia += 1
    valor -=5

print('----- Aula 37 -----')
#Operador Ternário - Programa que checa se a pessoa pode ou não votar nas eleições.
idade = 14

if (idade >= 16):
    resultado = print('Pode votar')
else:
    resultado = print('Não pode votar - Else')

resultado = 'Pode votar' if idade >= 16 else 'Não pode votar'
print(resultado + ' - Operador Ternário')

# A39 - Break - Fazer um programa que calcula a comissão de um produto acima de R$ 20 publicado no site
valor = int (input ('Insira o valor do seu produto:'))

print(valor)

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R$ {valor}')
    break