# 10 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Informe o Número Total de Eleitores: '))

candidato_a = 0
candidato_b = 0
candidato_c = 0

for i in range (1,eleitores+1):
    votar = int(input(f'Eleitor {i} em Quem Você Quer Votar?\n1 - Candidato (A)\n2 - Candidato (B)\n3 - Candidato (C)\nInforme: '))

    if votar == 1:
        candidato_a += 1
    elif votar == 2:
        candidato_b += 1
    elif votar == 3:
        candidato_c += 1

votar = candidato_a + candidato_b + candidato_c

print(f'Total de Eleitores: {eleitores}\nVotos Computados: {votar}')
print(f'Candidato (A) - {candidato_a} Votos\nCandidato (B) - {candidato_b} Votos\nCandidato (C) - {candidato_c} Votos')
































