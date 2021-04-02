# 6 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:

# Até 5Kg                    Acima de 5Kg
# Morango  R$ 2,50 por Kg    R$ 2,20 por Kg
# Maça     R$ 1,80 por Kg    R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

print('=================Sistema de Frutaria====================')

morango = int(input('-> Informe Quantos Kg de Morango Deseja Comprar: '))
maca = int(input('-> Informe Quantos Kg de Maçã Deseja Comprar: '))
print('================================================================')
kgs_fruta = (morango + maca) #Quantidade total de Kg entre Morango e Maça

if morango <= 5:
    valor_morango = (morango * 2.50) #Preço do Morango até 5Kg
    print(f'O Valor a ser Pago por {morango}Kg de Morango Será de: R${valor_morango:.2f}')
else:
    valor_morango = (morango * 2.20) #Preço do Morango acima de 5Kg
    print(f'O Valor a ser Pago por {morango}Kg de Morango Será de: R${valor_morango:.2f}')
if maca <= 5:
    valor_maca = (maca * 1.80) #Preço da Maçã até 5Kg
    print(f'O Valor a ser Pago por {maca}Kg de Maça Será de: R${valor_maca:.2f}')
else:
    valor_maca = (maca * 1.50) #Preço da Maçã acima de 5Kg
    print(f'O Valor a ser Pago por {maca}Kg de Maça Será de: R${valor_maca:.2f}')

valor_compra = valor_morango + valor_maca #Valor Total da compra

if kgs_fruta > 8 or valor_compra > 25:
    desconto = (valor_compra*10)/100 #Desconto de 10%
    valor_c_desconto = (valor_compra - desconto)
    print('================================================================')
    print(f'O Valor Total a ser Pago com Desconto Será de R${valor_c_desconto:.2f}') #Valor total da compra com desconto
else:
    print('================================================================')
    print(f'O Valor Total a ser Pago pela Compra Será de R${valor_compra:.2f}') #Valor total da compra sem o desconto










