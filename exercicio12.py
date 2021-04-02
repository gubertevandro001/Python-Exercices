# 12 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

numero_cds = int(input('Quantos CDs Você Possui em Sua Coleção?: '))

valor_total = 0
valor_medio = 0

for i in range (1,numero_cds+1):
    valor_cd = float(input(f'Quanto Custou o {i}° CD? R$: '))

    valor_total += valor_cd
    valor_medio += valor_cd / numero_cds

print(f'O Total Gasto em {numero_cds} CDs Foi de: R$ {valor_total}')
print(f'O Valor Médio Pago em Cada CD foi de: R$ {valor_medio:.2f}')


