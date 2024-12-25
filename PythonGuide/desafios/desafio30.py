'''

Crie uma função lambda que aceite dois números e retonre a multiplicação desses números.

'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

multiplicacao = lambda num1, num2: num1 * num2
print(multiplicacao(num1, num2))