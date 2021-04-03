# 30 - O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já
# é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de
# pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

#Preço do pão: R$ 0.18
#Panificadora Pão de Ontem - Tabela de preços
#1 - R$ 0.18
#2 - R$ 0.36
#...
#50 - R$ 9.00

quantidade_paes = int(input('Informe A Quantidade de Pães Que Deseja: '))
preco_pao = float(input('Informe o Valor de Cada Pão R$: '))

print('='*40)
print(f'Preço do Pão: R$ {preco_pao:.2f}')
print('Panificadora Pão de Ontem - Tabela de Preços:')

for count in range (1, quantidade_paes + 1):
    print(f'{count} - R$ {count * preco_pao:.2f}')
