# 6 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por
# quais número ele é divisível.

num = int(input("Digite um Número Inteiro Para Saber se é Primo: "))
cont = 0
div = []

for i in range(num):
    if num % (i + 1) == 0:
        cont += 1
        div.append(i + 1)
    else:
        cont

if cont == 2:
    print(f'O Número é Primo e é Divisível Por: {div}')
else:
    print(f'O Número Não é Primo Pois é Divisível Por: {div}')