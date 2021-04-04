# 40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados

# a - Código da cidade;
# b - Número de veículos de passeio (em 1999);
# c - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e - Qual a média de veículos nas cinco cidades juntas;
# f - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

codigos_cidades = []
numero_veiculos = []
numero_acidentes = []
acidentes_2000 = []

for count in range (1, 5 + 1):
    codigo_cidade = int(input(f'Digite o Código da {count}° Cidade: '))
    while codigo_cidade in codigos_cidades:
        print('Código Já Informado! Não Repita!')
        codigo_cidade = int(input('Digite Outro Código: '))

    n_veiculos = int(input('Número de Veículos de Passeio dessa Cidade em 1999: '))
    n_acidentes = int(input('Número de Acidentes em 1999: '))

    if n_veiculos > 2000:
        acidentes_2000.append(n_acidentes)
        numero_acidentes.append(n_acidentes)
    else:
        numero_acidentes.append(n_acidentes)

    numero_veiculos.append(n_veiculos)
    codigos_cidades.append(codigo_cidade)

menor_indice = numero_acidentes.index(min(numero_acidentes))
maior_indice = numero_acidentes.index(max(numero_acidentes))

print(f'Menos Acidentes: {min(numero_acidentes)}\nCódigo da Cidade: {codigos_cidades[menor_indice]}')
print(f'Mais Acidentes: {max(numero_acidentes)}\nCódigo da Cidade: {codigos_cidades[maior_indice]}')

media_veiculos = sum(numero_veiculos) / len(numero_veiculos)
print(f'Média de Veículos nas 5 Cidades: {media_veiculos:.0f}')

media_acidentes = sum(acidentes_2000) / len(acidentes_2000)
print(f'Média de Acidentes nas Cidades com Menos de 2000 Veículos: {media_acidentes:.0f}')
