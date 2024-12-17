#CLASSSES
#utilizadas para criar objetos/instancias
#sao utilizadas para agrupar dados e funções podendo realizar

import datetime  # Importa o módulo datetime

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def ano_nascimento(self):
        ano_atual = datetime.datetime.now().year  # Acessa a classe datetime dentro do módulo
        self.ano_nascimento = int(ano_atual - self.idade)
        return self.ano_nascimento
        
pessoa1 = Pessoa('Rennan', 'Carneiro', 21)  
anoPessoa1 = Pessoa.ano_nascimento(pessoa1)     

print(pessoa1.nome_completo(), anoPessoa1)
