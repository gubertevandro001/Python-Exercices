#6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
#ele mostre os números um ao lado do outro.

from time import sleep

print('=====Números de 1 a 20======')

for count in range (1, 21):
    print(count)
    sleep(0.5)


for count in range (1, 21):
    print(f'{count}', end=' ')
    sleep(0.5)
