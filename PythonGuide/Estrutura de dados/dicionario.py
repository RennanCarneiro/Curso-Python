# Introdução a Dicionários
# Dicionários utilizam index no formato de keys e de values, e aceitam string, int, float, boolean.

aluno = {'nome': 'Ana', 'idade': 16, 'nota final': 'A', 'aprovação': True}
# nome = key | Ana = value .... idade = key | 16 = value etc.

print(aluno['nome'])  # Pois usa o index no formato de keys e values

# Atualizando o Dicionário

aluno = {'nome': 'Ana', 'idade': 16, 'nota final': 'A', 'aprovação': True}

aluno['nome'] = 'José'
print(aluno['nome'])

aluno.update({'nome': 'José', 'nota final': 'B'})  # Atualiza mais de um ao mesmo tempo
print(aluno)

aluno.update({'nome': 'José', 'nota final': 'B', 'endereco': 'Rua A'})  # Além de atualizar, também adiciona.
print(aluno)

print(aluno.get('nome', 'não existe') + ' - método get')

del aluno['idade']
print(aluno)

# Looping dentro de um dicionário

for i in aluno:
    print(aluno[i])

print()

for i in aluno.values():
    print(i)

print()

for keys, values in aluno.items():
    print(keys, values)

# Visualizando Itens, Keys e Values

aluno = {'nome': 'Ana',
         'idade': 16,
         'nota final': 'A',
         'aprovação': True,
         'materias': ['Fisica', 'Matematica', 'Inglês']
         }

print(aluno.get('materias'))  # Mostra as 3 matérias que ela faz
print(len(aluno))  # Mostra a quantidade de keys (5)
print(aluno.keys())  # Mostra as keys
print(aluno.values())  # Mostra os values
print(aluno.items())  # Mostra os itens (keys e values)
