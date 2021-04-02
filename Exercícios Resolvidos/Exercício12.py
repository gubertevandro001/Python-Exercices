#12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário
#deve informar de qual numero ele deseja ver a tabuada.

numero = int(input('Informe Um Número Para Calcularmos Sua Tabuada: '))

while numero < 0 or numero > 10:
    print('Informe Números Somente de 0 a 10!')
    numero = int(input('Informe Um Número Para Calcularmos Sua Tabuada: '))
else:
    for count in range (1, 11):
        print(f'{numero} x {count} = {numero*count}')
