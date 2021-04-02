#11 - Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Informe o Primeiro Número: '))
num2 = int(input('Informe o Segundo Número: '))

soma = 0

for num in range (num1+1, num2):
    soma += num
print(f'A Soma dos Números Entre {num1} a {num2} é: {soma}')
