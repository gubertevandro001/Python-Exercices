# 24 - Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
count = 0
count1 = 0

while True:
    print('11 - Encerrar')
    count1 += 1
    notas = float(input(f'Informe a {count1}° Nota: '))
    print('='*50)

    if notas == 11:
        break
    count += 1
    soma += notas

media = soma / count

print(f'A Média Entre as {count} Notas é de: {media:.1f}')
print(f'A Soma das Notas é de: {soma}')
