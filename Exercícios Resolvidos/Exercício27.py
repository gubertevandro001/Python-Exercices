# 27 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input('Informe a Quantidade de Turmas: '))
print('-'*50)

media = 0

for i in range (1, turmas + 1):
    alunos = int(input(f'Informe O Total de Alunos da Turma {i}: '))
    print('-'*50)

    while alunos > 40:
        print('O Número Máximo Permitido de Alunos Por Turma é 40!')
        alunos = int(input(f'Informe O Total de Alunos da Turma {i}: '))
    else:
        media += alunos / turmas

print(f'A Média de Alunos Por Sala é de: {media:.0f}')
