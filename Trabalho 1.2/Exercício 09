# 9 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme
# a média calculada.

soma = 0
media = 0
count = 0

while True:
    idade = int(input('0 - Finaliza\n''Informe a Idade da Pessoa: '))

    if idade == 0:
        break
    else:
        soma += idade
        count += 1

media = soma / count

if media <=25:
    print(f'Jovens!\nMedia = {media:.0f}') #Utilizei (:.0f) Para Especificar Média de Idades Sendo Inteira
elif media > 25 and media <= 60:
    print(f'Adultos!\nMedia = {media:.0f}') #Utilizei (:.0f) Para Especificar Média de Idades Sendo Inteira
elif media > 60:
    print(f'Idosos!\nMedia = {media:.0f}') #Utilizei (:.0f) Para Especificar Média de Idades Sendo Inteira

