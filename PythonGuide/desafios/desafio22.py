'''

Crie uma lista com 5 nomes de países e suas capitais. Peça ao usuário para digitar o nome de um país.
Se o país estiver na lista, imprima "A capital de [país] é [capital]". Se o país não estiver na lista,
imprima "Desculpe, não temos informações sobre a capital desse país.".

'''

capitais = {
    'Brasil' : 'Brasília',
    'EUA' : 'Washington',
    'França' : 'Paris',
    'Alemanha' : 'Berlim',
    'China' : 'Pequim'
}

usuario = input("Digite o nome de um país: ")
if usuario in capitais:
    print(f"A capital de {usuario} é {capitais[usuario]}.")
else:
    print("Desculpe, não temos informações sobre a capital desse país.")