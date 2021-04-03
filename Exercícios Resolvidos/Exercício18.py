#18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numero_repetir = int(input('Digite um Número de Vezes a Repetir: '))

lista_numeros = []

for i in range (1,numero_repetir+1):
    numero = lista_numeros.append(int(input(f'Informe Número {i}/{numero_repetir}: ')))

print(f'O Maior Número é: {max(lista_numeros)}')
print(f'O Menor Número é: {min(lista_numeros)}')
print(f'A Soma de Todos os Números é: {sum(lista_numeros)}')
