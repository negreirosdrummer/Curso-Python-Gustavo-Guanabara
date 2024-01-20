# CRIE UM PROGRAMA QUE DECLARE UMA MATRIZ DE DIMENSÃO 3x3 E PREENCHA COM VALORES LIDOS PELO TECLADO.
# NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMATAÇÃO CORRETA

# MINHA RESOLUÇÃO
matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        num = int(input(f'Digite um valor para a posição [{i}, {j}]: '))
        matriz[i].append(num)
print('-=' * 22)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == len(matriz) - 1:
            print(f'[{matriz[i][j]:^5}]')
        else:
            print(f'[{matriz[i][j]:^5}]', end=' ')


# MINHA RESOLUÇÃO ANTIGA
'''matriz = [[], [], []]
for i in range(len(matriz)):
    for j in range(0, 3):
        valor = int(input(f"Digite um valor para a posição [{i}, {j}]: "))
        matriz[i].append(valor)

print("-="*30)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'[\t{matriz[i][j]}\t]', end='')
        if j == 2:
            print()'''


# RESOLUÇÃO GUANABARA
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i}, {j}]: "))
print("-=" * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()'''
