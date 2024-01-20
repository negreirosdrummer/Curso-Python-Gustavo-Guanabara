# APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
# A SOMA DE TODOS OS VALORES PARES DIGITADOS
# A SOMA DOS VALORES DA TERCEIRA COLUNA
# O MAIOR VALOR DA SEGUNDA LINHA

# MINHA RESOLUÇÃO
matriz = [[], [], []]
soma_pares = soma_3col = maior_2lin = 0
for i in range(3):
    for j in range(3):
        num = int(input(f'Digite um valor para a posição [{i}, {j}]: '))
        if num % 2 == 0:
            soma_pares += num
        if j == 2:
            soma_3col += num
        matriz[i].append(num)

print('-=' * 30)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == 1:
            maior_2lin = matriz[i][j]
        elif matriz[1][j] > maior_2lin:
            maior_2lin = matriz[1][j]
        if j == len(matriz) - 1:
            print(f'[{matriz[i][j]:^5}]')
        else:
            print(f'[{matriz[i][j]:^5}]', end=' ')
print('-=' * 30)

print(f'A soma dos valores pares digitados é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_3col}')
print(f'O maior valor da segunda linha é {maior_2lin}')


# RESOLUÇÃO GUANABARA
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma3col = maior2lin = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i}, {j}]: "))
print("-="*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
    print()
print("-="*30)
print(f'A soma dos valores pares é {soma_pares}')
for i in range(0, 3):
    soma3col += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {soma3col}')
for j in range(0, 3):
    if j == 0:
        maior2lin = matriz[1][j]
    elif matriz[1][j] > maior2lin:
        maior2lin = matriz[1][j]
print(f'O maior valor da segunda linha é {maior2lin}')'''
