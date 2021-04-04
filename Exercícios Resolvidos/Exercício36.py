# 36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas
# a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
# também pelo usuário, conforme exemplo abaixo:

#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35

tabuada = int(input('Mostrar a Tabuada do: '))
comecar = int(input('Começar Por: '))
terminar = int(input('Terminar em: '))

while terminar < comecar:
    print('Valor Final Deve Ser Maior Que o Inicial!')
    comecar = int(input('Começar Por: '))
    terminar = int(input('Terminar em: '))
else:
    print(f'Vou Montar a Tabuada de {tabuada} Começando em {comecar} e Terminando em {terminar}:')

    for i in range(comecar, terminar + 1):
        print(f'{tabuada} x {i} = {tabuada * i}')
