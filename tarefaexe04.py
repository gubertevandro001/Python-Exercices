#4 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
#positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".

p1 = int(input('Telefonou para a vítima?\n1 - Sim ou 2 - Não: '))
p2 = int(input('Esteve no local do crime?\n1 - Sim ou 2 - Não: '))
p3 = int(input('Mora perto da vítima?\n1 - Sim ou 2 - Não: '))
p4 = int(input('Devia para a vítima?\n1 - Sim ou 2 - Não: '))
p5 = int(input('Já trabalhou com a vítima?\n1 - Sim ou 2 - Não: '))

list = [p1, p2, p3, p4, p5]

if list.count(1) == 2:
    print('Você é Suspeito!!')
elif list.count(1) == 3 or list.count(1) == 4:
    print('Você é Cúmplice!!')
elif list.count(1) == 5:
    print('Você é o Assassino!!')
else:
    print('Você é Inocente!!')





