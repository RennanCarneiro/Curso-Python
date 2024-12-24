'''

Criar uma lista de frutas que inclui "maçã" três vezes e outras frutas de sua escolha.
Use um for loop para contar quantas vezes "maçã" aparece na lista e imprima o resultado.

'''

frutas = ['banana', 'maçã', 'laranja', 'uva', 'manga', 'abacaxi', 'maçã', 'maçã', 'maçã']

count = 0

for i in frutas:
    if i ==  'maçã':
        count += 1
        
print(f"O número de vezes que a maçã aparece na lista é: {count}")