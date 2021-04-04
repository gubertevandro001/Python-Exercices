# 31 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
# conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber
# um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo
# operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em
# dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

from time import sleep

while True:
    calcular_preco = True
    valor_total = 0
    count = 0
    print('=====Lojas Tabajara=====\n')

    while calcular_preco:
        count += 1
        valor_produto = float(input(f'Produto {count} R$: '))
        valor_total += valor_produto

        if valor_produto == 0:
            print(f'Total R$: {valor_total:.2f}')
            break

    dinheiro = float(input('Dinheiro R$: '))

    while dinheiro < valor_total:
        print('Dinheiro Insuficiente!')
        dinheiro = float(input('Dinheiro R$: '))
    else:
        print(f'Troco R$: {dinheiro - valor_total:.2f} ')

    continuar = input('Você Deseja Continuar Comprando?\n(S) - Sim\n(N) - Não\nInforme: ')

    if continuar in 'sS':
        print('Retornando ao Caixa...\n')
        sleep(3)
    elif continuar in 'nN':
        print('Compras Encerradas!')
        break

