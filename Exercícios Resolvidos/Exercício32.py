# 32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input('Digite um Número Inteiro Para Vermos o Seu Fatorial: '))

fatorial = num

print(f'Fatorial de: {num}')
print(f'{num}! = {num}', end='')

for count in range(num - 1, 0, -1):
    print(f'.{count}', end='')
    fatorial *= count
print(f' = {fatorial}', end='')
