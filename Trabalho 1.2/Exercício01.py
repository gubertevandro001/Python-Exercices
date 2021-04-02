#1 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Informe um Número Inteiro Para Vermos o Seu Fatorial: '))

fatorial = numero

for count in range (numero-1, 0, -1):
    fatorial *= count

print(f'O Fatorial do Número {numero} é: {fatorial}')
