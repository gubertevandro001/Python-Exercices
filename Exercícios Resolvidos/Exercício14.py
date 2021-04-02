#14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
# de números impares.

par = 0
impar = 0
count = 0

for i in range (1, 11):
    num = int(input(f'Informe Número {i}/10: '))
    if num % 2 == 0:
        par += 1
        count += par + 1
    else:
        impar += 1
        count += impar + 1

print(f'Dos 10 Números Informados:\nSão Pares: {par}\nSão Ímpares: {impar}')



