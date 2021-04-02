#3 - Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input('Informe seu Nome: ')
idade = int(input('Informe sua Idade: '))
salario = float(input('Informe o Seu Salário: '))
sexo = input('Informe seu Sexo M - Masculino F - Feminino: ')
estado_civil = input('Informe seu Estado Civil S - Solteiro C - Casado V - Víuvo D - Divorciado: ')

while len(nome) < 3 or idade > 150 or salario < 0 or sexo != 'M' and sexo != 'F' or estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V'  and estado_civil != 'D':
    print("Verifique as Informações Que Você Digitou e Tente Novamente!")
    nome = input('Informe seu Nome: ')
    idade = int(input('Informe sua Idade: '))
    salario = float(input('Informe o Seu Salário: '))
    sexo = input('Informe seu Sexo M - Masculino F - Feminino: ')
    estado_civil = input('Informe seu Estado Civil S - Solteiro C - Casado V - Víuvo D - Divorciado: ')

print(f'Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado Civil: {estado_civil}')
