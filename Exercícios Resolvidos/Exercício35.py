# 35 - Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.

numero = int(input('Informe um Número Para Vermos os Primos Entre Ele: '))
print('='*100)

lista = []

for count in range (numero + 1):
    if count % 2 == 1 and count != 2:
        lista.append(count)

print(f'Os Números Primos Entre o Número 1 Até o Número {numero} São: {lista}')
