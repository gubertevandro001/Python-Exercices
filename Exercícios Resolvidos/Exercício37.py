# 37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
# mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua
# altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais
# gordo e do mais magro, além da média das alturas e dos pesos dos clientes

cod_clientes = []
altura_clientes = []
peso_clientes = []
count = 1
codigo = True

while True:
    print(f'Cliente N° {count}')
    codigo = int(input('Digite Seu Código: '))
    if codigo == 0:
        break
    else:
        altura = float(input('Digte Sua Altura: '))
        peso = float(input('Digite Seu Peso: '))
        cod_clientes.append(codigo)
        altura_clientes.append(altura)
        peso_clientes.append(peso)
        count += 1

cod_magro = peso_clientes.index(min(peso_clientes))
cod_gordo = peso_clientes.index(max(peso_clientes))
cod_alto = altura_clientes.index(max(altura_clientes))
cod_baixo = altura_clientes.index(min(altura_clientes))
print('\n' * 2)
print(f'Código do Mais Magro: {cod_clientes[cod_magro]}\nPeso: {min(peso_clientes)}')
print(f'Código do Mais Gordo: {cod_clientes[cod_gordo]}\nPeso: {max(peso_clientes)}')
print(f'Código do Mais Alto: {cod_clientes[cod_alto]}\nAltura: {max(altura_clientes)}')
print(f'Código do Mais Baixo: {cod_clientes[cod_baixo]}\nAltura: {min(altura_clientes)}')
print(f'Média de Altura: {sum(altura_clientes) / len(altura_clientes)}')
print(f'Média de Peso: {sum(peso_clientes) / len(peso_clientes)}')
