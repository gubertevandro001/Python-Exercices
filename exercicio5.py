#5 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele
# que é divisível somente por ele mesmo e por 1.

numero = int(input('Digite um Número Inteiro Para Vermos se Ele é Primo: '))

count = 0

for i in range (1, numero+1):
    if numero % i == 0:
        count += 1

print('É PRIMO!' if count == 2 else 'NÃO É PRIMO!')