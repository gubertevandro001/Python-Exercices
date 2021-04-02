#10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Informe o Primeiro Número: '))
num2 = int(input('Informe o Segundo Número: '))

while num2 < num1:
    print('O Segundo Número Deve Ser Maior do Que o Primeiro!')
    num1 = int(input('Informe o Primeiro Número: '))
    num2 = int(input('Informe o Segundo Número: '))
else:
    print(f'Os Números Inteiros Entre {num1} a {num2} São:')
    for num in range(num1+1, num2):
        print(num, end= ' ')

