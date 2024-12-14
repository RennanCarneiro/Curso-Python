from array import array

# Arrays
# Utiliza-se Arrays quando uma lista é muito grande.

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])  # u -> string
inteiros = array('i', [10, 20, 30, 40])    # i -> integer
float = array('f', [1.2, 2.2, 3.2])        # f -> float

print(letras)
print(inteiros)
print(float)

# Criando Sets
# Set é similar a listas, evita itens duplicados e não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)  # | = Union. Une as listas sem repetir valores.
print(num1 - num2)  # - = Difference. Mostra apenas os números exclusivos da lista 1.
print(num1 ^ num2)  # ^ = Symmetric Difference. Une as listas e exclui os valores repetidos.
print(num1 & num2)  # & = And. Mostra apenas os itens duplicados nas listas.

print(len(num1))

# Funções em Sets

list1 = set([1, 2, 3, 4, 5, 6])

s1 = {1, 2, 3, 4, 5, 6, 1, 2, 3}

s1.add(7)
s1.add(1)
s1.update([1, 2, 8, 9])  # ignora o 1 e o 2 pois já existiam.
s1.remove(9)
s1.discard(8)
# remove e discard fazem a mesma coisa, só que remove dá erro se o item não estiver no set.

print(s1)

# Sets com Strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
print(f'{set4} - Union')  # Une os sets.

set4 = set1.difference(set3)
print(f'{set4} - Difference')  # Mostra os elementos exclusivos do set1.

set4 = set1.intersection(set2)
print(f'{set4} - Intersection')  # Mostra os elementos em comum.

set4 = set1.symmetric_difference(set3)
print(f'{set4} - Symmetric Difference')  # Une os sets e remove duplicados.
