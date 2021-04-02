# 5 -Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e
# imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
# é R$ 2,50 o preço do litro do álcool é R$ 1,90.

tipo_combustivel = input('===Tipos de Combustíveis===\nA - (Álcool)\nG - (Gasolina)\nQual você deseja comprar?: ')
litros = int(input('Quantos litros você deseja?: '))
tipoCombustivel = str.upper(tipo_combustivel)

if tipoCombustivel == 'A' and litros <= 20:
    preco_litro = 1.90
    desconto_litro = 0.05 #Equivalente a 3% de desconto sobre o preço do Álcool
    litro_c_desconto = (preco_litro-0.05)
    print(f'O Valor a pagar pelo Álcool será de: R$ {(litros*litro_c_desconto):.2f}')

elif tipoCombustivel == 'A' and litros > 20:
    desconto_litro = 0.09 #Equivalente a 5% de desconto sobre o preço do Álcool
    print(f'O Valor a pagar por {litros}L de Álcool será de: R$ {(litros * 1.81):.2f}')

elif tipoCombustivel == 'G' and litros <=20:
    preco_litro = 2.50
    desconto_litro = 0.10 #Equivalente a 4% de desconto sobre o preço da Gasolina
    litro_c_desconto = (preco_litro - 0.10)
    print(f'O Valor a pagar por {litros}L de Gasolina será de: R$ {(litros * litro_c_desconto):.2f}')

elif tipoCombustivel == 'G' and litros > 20:
    desconto_litro = 0.15 #Equivalente a 6% de desconto sobre o preço da Gasolina
    print(f'O Valor a pagar por {litros}L de Gasolina será de: R$ {(litros * 2.35):.2f}')



