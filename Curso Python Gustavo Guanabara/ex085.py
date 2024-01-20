# DESAFIO 85
# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR SETE VALORES NUMÉRICOS E CADASTRE-OS EM
# UMA LISTA ÚNICA QUE MANTENHA SEPARADOS OS VALORES PARES E ÍMPARES.
# NO FINAL, MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE

# MINHA RESOLUÇÃO
geral = []
pares = []
impares = []
for c in range(7):
    num = int(input(f'Digite o {c + 1}ª valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
geral.append(pares[:])
geral.append(impares[:])
cont_pares = len(geral[0])
cont_impares = len(geral[1])
print('-=' * 30)
if cont_pares == 1:
    print(f'O valor par digitado foi {pares[0]}')
elif cont_pares > 1:
    print(f'Os valores pares digitados foram ', end='')
    for n in range(len(geral[0])):
        if cont_pares > 2:
            print(geral[0][n], end=', ')
            cont_pares -= 1
        elif cont_pares == 2:
            print(geral[0][n], end=' e ')
            cont_pares -= 1
        else:
            print(geral[0][n])

if cont_impares == 1:
    print(f'O valor ímpar digitado foi {impares[0]}')
elif cont_impares > 1:
    print(f'Os valores ímpares digitados foram ', end='')
    for n in range(len(geral[1])):
        if cont_impares > 2:
            print(geral[1][n], end=', ')
            cont_impares -= 1
        elif cont_impares == 2:
            print(geral[1][n], end=' e ')
            cont_impares -= 1
        else:
            print(geral[1][n])


# RESOLUÇÃO GUANABARA
'''num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')'''
