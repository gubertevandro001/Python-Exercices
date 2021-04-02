#3 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o seundo número: '))
pergunta = input('Qual das operações você deseja realizar?\n1 - (Subtração)\n2 - (Adição)\n3 - (Multiplicação)\n4 - (Divisão)\nInforme uma: ')

if pergunta == '1':
    resultado = (num1-num2)
elif pergunta == '2':
    resultado = (num1+num2)
elif pergunta == '3':
    resultado = (num1*num2)
elif pergunta == '4':
    resultado = (num1/num2)

print(f'Resultado = {resultado}')

if resultado % 2 == 0:
    print('O Número é par!')
else:
    print('O Número é ímpar!')
if resultado >= 0:
    print('O Número é positivo!')
else:
    print('O Número é negativo!')
if resultado == round(resultado):
    print('O Número é inteiro!')
else:
    print('O Número é decimal!')


