'''

Crie uma lista com os nomes de três cidades. Peça ao usuário para digitar o nome de uma cidade.
Se a cidade estiver na lista, imprima "A cidade está na lista". Caso contrário, imprima
"A cidade não está na lista."

Obs: Não pode usar list[]
'''

cidades = ('Recife', 'Olinda', 'Jaboatão dos Guararapes')

while True: # loop infinito para que o usuário possa tentar novamente caso a cidade não esteja na lista de cidades 
    cidade = input("Digite o nome de uma cidade: ")
    if cidade in cidades:
        print("A cidade está na lista.")
        break
    else:
        print("A cidade não está na lista.") 