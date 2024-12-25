'''

Crie dois conjuntos, cada um contendo 5 nomes. Alguns nomes devem estar presentes em ambos os conjuntos.
Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima o resultado.

Bônus: utilizar outros métodos além do intersection.

'''

nomes1 = {'João', 'Maria', 'José', 'Ana', 'Carlos'}
nomes2 = {'Maria', 'Ana', 'Pedro', 'Carlos', 'Bianca'}

nomes_comuns = nomes1.intersection(nomes2)
print(nomes_comuns)

# Bônus
nomes_comuns2 = nomes1 & nomes2
print(nomes_comuns2)

print(nomes1.union(nomes2)) # União dos conjuntos


print(nomes1.symmetric_difference(nomes2)) # Diferença simétrica

print(nomes1.difference(nomes2),' - São exclusivos da lista 1.') # Diferença entre os conjuntos 1
print(nomes2.difference(nomes1),' - São exclusivos da lista 2.') # Diferença entre os conjuntos 2 
