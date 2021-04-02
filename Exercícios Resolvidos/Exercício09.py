#9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

print('=====Números Ímpares Entre 1 a 50=====')

for num in range(0,51):
    if num % 2 != 0:
        print(num, end= ' ')
