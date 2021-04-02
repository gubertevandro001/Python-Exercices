# 8 - Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
media = 0
count = 0

while True:
    nota = float(input('(Caso Deseje Parar Digite 11)\nInforme uma Nota: '))
    if nota == 11:
        break
    soma += nota
    count += 1
media = soma / count

print(f'A Média Entre as {count} Notas Informadas Foi de: {media:.1f}')





