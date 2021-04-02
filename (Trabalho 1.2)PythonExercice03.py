#3 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

num_repetir = int(input('Digite um Número de Vezes a Repetir Até 1000: '))

maior = None
menor = None

while num_repetir > 1000:
    print('Digite Números a Repetir Até 1000!')
    num_repetir = int(input('Digite um Número de Vezes a Repetir Até 1000: '))
else:
    for count in range(num_repetir):
            numero = int(input('Informe um Número: '))
            maior = maior if maior != None and maior > numero else numero
            menor = menor if menor != None and menor < numero else numero

print(f'O Maior Número é {maior} e o Menor Número é {menor}!')

