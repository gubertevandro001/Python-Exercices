#2 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

num_repetir = int(input('Digite um Número de Vezes Para Repetir: '))

maior = None
menor = None

for i in range (num_repetir):
    numero = int(input('Informe um Número: '))
    maior = maior if maior != None and maior > numero else numero
    menor = menor if menor != None and menor < numero else numero

print(f'O Maior Número é {maior} e o Menor Número é {menor}!')
