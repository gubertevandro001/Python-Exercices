# 34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
# aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se
# ele é ou não um número primo.

numero = int(input('Informe um Número Para Vermos se Ele é Primo: '))

count = 0

for i in range (1, numero + 1):
    if numero % i == 0:
        count += 1

print(f'O Número {numero} é Primo!' if count == 2 else f'O Número {numero} Não é Primo!')
