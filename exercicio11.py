# 11 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turma = int(input('Informe o Número de Turmas: '))

media = 0

for i in range (1,turma+1):
    alunos = int(input(f'A Turma {i} Possui Quantos Alunos?: '))

    while alunos > 40:
        print('O Número Máximo de Alunos Permitidos Por Turma é 40!')
        alunos = int(input(f'A Turma {i} Possui Quantos Alunos?: '))
    else:
        media += alunos / turma

print(f'A Média de Alunos Por Sala é de: {media:.0f} Alunos') #Utilizei (:.0f) Para Especificar Média de Alunos Sendo Inteira
