'''

Imagine que você tem uma loja de carros, e crie uma lista com os carros que você tem em estoque.
Os carros são "Sandero","Gol","HB20". Peça ao usuário para que ele insira o nome do carro que deseja comprar.
Se o carro estiver em estoque, imprima "Este carro está disponível". Se o carro não estiver em estoque,
imprima "Desculpe, este carro não está disponível."

Bônus: trabalhar com lower case

'''

carros = ["Sandero", "Gol", "HB20"]
input = input("Digite o nome do carro que deseja comprar: ")

if input.lower() in carros: # lower case para não ter problemas com a entrada do usuário
    print("Este carro está disponível.")
else:
    print("Desculpe, este carro não está disponível.")