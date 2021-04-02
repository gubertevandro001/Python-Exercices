#2 -Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

numero = float(input('Informe um número: '))

if numero == round(numero):
    print('O Número é inteiro!')

else:
    print('O Número é decimal!')
    print('Arredondado para Baixo: ',round(numero - 0.5))
    print('Arredondado para Cima : ',round(numero + 0.5))

