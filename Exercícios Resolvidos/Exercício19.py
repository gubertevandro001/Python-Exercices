# 19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista_numeros = []
count = 0
count1 = 0

numeros_repetir = int(input('Digite um Número de Vezes a Repetir: '))

while numeros_repetir != count:
    count += 1
    numero = float(input(f'Informe Número {count}/{numeros_repetir}: '))

    while numero > 1000 or numero < 0:
        print('Número Inválido! Informe Números de 0 a 1000!')
        numero = float(input(f'Informe Número {count}/{numeros_repetir}: '))

    lista_numeros.append(numero)
    count1 += 1

print(f'O Maior Número é: {max(lista_numeros)}')
print(f'O Menor Número é: {min(lista_numeros)}')
print(f'A Soma Desses Números é: {max(lista_numeros) + min(lista_numeros)}')
