'''

Crie um loop que peça ao usuário para digitar o nome de uma fruta. Se a fruta digitada não for
"abacate", o loop deve continuar pedindo ao usuário para digitar o nome da fruta. Se a fruta for
"abacate", o loop termina e o programa imprime "Parabéns, você acertou a fruta!".

'''

fruta = input("Digite o nome de uma fruta: ")

while fruta != "abacate": # enquanto a fruta digitada não for "abacate"
    fruta = input("Digite o nome de uma fruta: ")
    
print("Parabéns, você acertou a fruta!") # se a fruta digitada for "abacate", o loop termina e essa mensagem é impressa