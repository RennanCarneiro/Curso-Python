'''
criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
o usuario irá fornecer as seguintes informações: rendimento, altura e largura.
o programa deve mostra na tela a mensagem *você necessita X latas de tinta*
'''
rendimento = int(input("Qual o rendimento da lata? "))
altura = int(input("Qual a altura da parede? "))
largura = int(input("Qual a largura da parede? "))

def calculo_tinta():
    area = area * altura
    total = area / rendimento
    print(f"Você precisa de {total} latas de tintas")
    
calculo_tinta