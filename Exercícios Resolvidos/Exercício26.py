# 26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
# cada eleitor votar e ao final mostrar o número de votos de cada candidato.

numero_eleitores = int(input('Informe o Total de Eleitores: '))

candidato_a = 0
candidato_b = 0
candidato_c = 0

for count in range(1, numero_eleitores + 1):
    voto_eleitor = int(input(f'Eleitor Número {count} em Quem Você Deseja Votar?\n(1) - Candidato A\n(2) - Candidato B\n(3) - Candidato C\nInforme: '))

    if voto_eleitor == 1:
        candidato_a += 1
    elif voto_eleitor == 2:
        candidato_b += 1
    elif voto_eleitor == 3:
        candidato_c += 1

voto_eleitor = candidato_a + candidato_b + candidato_c

print(f'Total de Eleitores: {numero_eleitores}')
print(f'Votos Computados: {voto_eleitor}')
print(f'Candidato (A) = {candidato_a} Votos\nCandidato (B) = {candidato_b} Votos\nCandidato (C) = {candidato_c} Votos')
