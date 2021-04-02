#13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
#número. Não utilize a função de potência da linguagem.

base = int(input('Informe o Número Base: '))
expoente = int(input('Informe o Número Expoente: '))

potencia = 1
count = 0

while count < expoente:
    potencia *= base
    count += 1
print(f'A Potência do Número {base} Elevado ao Número {expoente} é de: {potencia}')

