# 23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero_range = int(input('Informe um Número Para Vermos os Números Primos Entre ele: '))
print('='*50)

for numero in range (1, numero_range + 1):

    count = 0

    for j in range (1, numero + 1):
        if numero % j == 0:
            count += 1

    print(f'O Número {numero} é Primo' if count == 2 else f'O Número {numero} Não é Primo!')
    print(f'Realizou {numero + 1} Divisões!')
    print('='*50)
