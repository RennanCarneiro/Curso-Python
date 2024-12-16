#erros
#excelente para testes
    #nao realiza o stop no programa
    #mensagens customizadas
    
try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print("Index inexistente")
    
#trabalhando com input
try:
    valor = int(input('Digite um valora: '))
    print(valor)
except ValueError:
    print('Só permitido numeros')
#else:
#    print('Usuario digito corretamente')
finally:
    print('codigo ok')