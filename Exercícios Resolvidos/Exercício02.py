#2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
#uma mensagem de erro e voltando a pedir as informações.

login = input('Login: ')
senha = input('Senha: ')

while senha == login:
    print('Senha Deve Ser Diferente de Login! Tente Novamente!')
    login = input('Login: ')
    senha = input('Senha: ')
else:
    print('Logado Com Sucesso!!')
