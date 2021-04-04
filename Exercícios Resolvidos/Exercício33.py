# 33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como
# a média das temperaturas.

quant_temperaturas = int(input('Informe a Quantia de Temperaturas Que Deseja: '))
print('='*50)

n_temperaturas = []

for count in range (1, quant_temperaturas + 1):
    temperaturas = float(input(f'Informe a Temperatura {count}/{quant_temperaturas}: '))

    n_temperaturas.append(temperaturas)

print('='*50)
print(f'A Maior Temperatura é: {max(n_temperaturas):.1f}ºC\nA Menor Temperatura é: {min(n_temperaturas):.1f}ºC')
print(f'A Média das Temperaturas é de: {sum(n_temperaturas)/quant_temperaturas:.1f}°C')

