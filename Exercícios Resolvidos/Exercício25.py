# 25 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme
# a média calculada.

soma = 0
count = 0
count1 = 0

while True:
    print('0 - Encerrar')
    count1 += 1
    idade = int(input(f'Informe a {count1}º Idade: '))
    print('-'*50)

    if idade == 0:
        break
    soma += idade
    count += 1

media = soma / count

if media <= 25:
    print(f'Jovens!!\nMédia = {media:.0f}')
elif media > 25 and media < 60:
    print(f'Adultos!!\nMédia = {media:.0f}')
elif media > 60:
    print(f'Idosos!!\nMédia = {media:.0f}')
