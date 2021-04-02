#15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
#série até o n−ésimo termo

print('==========Sequência de Fibonacci==========')
print('===========10 Primeiros Termos==============')

n_termo = 10   #Altere o valor dos termos para qual quiser, coloquei apenas 10 para não ficar tão extenso.
ultimo = 0
penultimo = 1
count = 0

for i in range (0, n_termo):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    print(termo, end=' ')
