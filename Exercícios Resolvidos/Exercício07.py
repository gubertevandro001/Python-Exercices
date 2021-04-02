#7 - Faça um programa que leia 5 números e informe o maior número.

maior = 0

for num in range (1,6):
    numero = float(input(f'Informe Número {num}/5: '))
    if numero > maior:
        maior = numero
print(f'O Maior Número Entre os 5 Números Informados é: {maior}')
