#8 - Faça um programa que leia 5 números e informe a soma e a média dos números.

media = 0
soma = 0

for num in range (1,6):
    numero = float(input(f'Informe Número {num}/5: '))
    soma += numero
    media = soma / 5

print(f'A Soma Dos Números é de: {soma}\nA Média Entre os Números é: {media}')
