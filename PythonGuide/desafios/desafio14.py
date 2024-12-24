'''

Criar um loop que imprima os números de 1 a 10, mas pare de imprimir assim que chegar a 5 usando
o comando "break". Em seguida, criar um segundo loop que imprima os números de 1 a 10, mas pule
a impressão do 5 usando o comando "continue"

'''

for i in range(1, 11):
    if i == 5: # se i for igual a 5
        break # interrompe o loop
    print(i) # imprime i
    
for i in range(1, 11):
    if i == 5: # se i for igual a 5
        continue # pula a impressão de 5
    print(i) # imprime i