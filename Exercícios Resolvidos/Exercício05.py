#5 -Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
# # entrada e permita repetir a operação.

pop_a = float(input('Informe a População Total do País A: '))
pop_b = float(input('Informe a População Total do País B: '))
taxa_a = float(input('Informe a Taxa de Crescimento Anual da População do País A: '))
taxa_b = float(input('Informe a Taxa de Crescimento Anual da População do País B: '))

anos = 0

while pop_a <= pop_b:
    pop_a += pop_a * taxa_a / 100
    pop_b += pop_b * taxa_b / 100
    anos += 1

print(f'O País A Ultrapassa ou Iguala-se ao País B em {anos} anos!')
