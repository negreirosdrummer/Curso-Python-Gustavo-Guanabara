# DESAFIO 50
# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
# SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O

soma = 0
cont = 0
for c in range(0, 6):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont > 1:
    print(f'Você informou {cont} números pares e a soma desses números é {soma}')
elif cont == 1:
    print(f'Você informou somente {cont} número par e a soma é {soma}')
elif cont == 0:
    print(f'Você não informou nenhum número par!')
