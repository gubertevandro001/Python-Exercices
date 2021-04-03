# 22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais
# números ele é divisível.

numero = int(input('Informe um Número Para Sabermos se Ele é Primo: '))
divisivel = []

count = 0

for i in range (numero):
    if numero % (i + 1) == 0:
        count += 1
        divisivel.append(i + 1)
    else:
        count += 0

if count == 2:
    print(f'O Número {numero} é Primo e é Divisível por: {divisivel}')
else:
    print(f'O Número {numero} Não é Primo pois é Divisível por: {divisivel}')
