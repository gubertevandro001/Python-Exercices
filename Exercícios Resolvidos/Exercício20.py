# 20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando
# o fatorial a números inteiros positivos e menores que 16

calcular_fatorial = True
continuar = True

while calcular_fatorial:
    numero = int(input('Digite um Número Para Calcularmos o Seu Fatorial: '))

    if numero > 16:
        print('Número Inválido! Informe Números Até 16!')
    else:
        fatorial = numero

        for count in range (numero-1, 1, -1):
            fatorial *= count

        print(f'O Fatorial do Número {numero} é: {fatorial}')

    while continuar:
        continuar_calculando = input('Você Deseja Continuar Calculando Fatoriais?\n(S) - Sim\n(N) - Não\nInforme: ')

        if continuar_calculando in 'sS':
            calcular_fatorial = True
            break
        elif continuar_calculando in 'nN':
            print('Programa Finalizado!')
            calcular_fatorial = False
            break



