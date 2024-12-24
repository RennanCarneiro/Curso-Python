'''

Crie uma lista de frutas e outra de vegetais. Use um for loop aninhado (nested for loop) para imprimir
todas as combinações possíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo.

Criar uma lista de 3 frutas e outra de 3 vegetais

'''

frutas = ['banana', 'maçã', 'laranja', 'uva', 'manga', 'abacaxi']
vegetais = ['alface', 'rúcula', 'agrião', 'espinafre', 'acelga', 'repolho']

for i in frutas: # para cada fruta
    for j in vegetais: # para cada vegetal
        print(i, j) # imprime a combinação de fruta e vegetal