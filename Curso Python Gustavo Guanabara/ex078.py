# DESAFIO 78
# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA.
# NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA

# MINHA RESOLUÇÃO
lista = []
maior = 0
menor = 0
for c in range(5):
    lista.append(int(input(f'Digite o {c + 1}º valor: ')))
    if c == 0:
        maior = menor = lista[c]
    elif c > 0:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
print('-=' * 20)
print(f'Você digitou os valores ', end='')
for n in range(len(lista)):
    if n < len(lista) - 2:
        print(f'{lista[n]}', end=', ')
    elif n < len(lista) - 1:
        print(f'{lista[n]}', end=' e ')
    else:
        print(f'{lista[n]}')

pos_maiores = []
pos_menores = []
for i, n in enumerate(lista):
    if lista[i] == maior:
        pos_maiores.append(i + 1)
    elif lista[i] == menor:
        pos_menores.append(i + 1)

if len(pos_maiores) == 1:
    print(f'O maior valor é {maior}, na posição {pos_maiores[0]}')
elif len(pos_maiores) > 1:
    print(f'O maior valor é {maior}, nas posições ', end='')
    for n in range(len(pos_maiores)):
        if n < len(pos_maiores) - 2:
            print(f'{pos_maiores[n]}', end=', ')
        elif n < len(pos_maiores) - 1:
            print(f'{pos_maiores[n]}', end=' e ')
        else:
            print(f'{pos_maiores[n]}')

if len(pos_menores) == 1:
    print(f'O menor valor é {menor}, na posição {pos_menores[0]}')
elif len(pos_menores) > 1:
    print(f'O menor valor é {menor}, nas posições ', end='')
    for n in range(len(pos_menores)):
        if n < len(pos_menores) - 2:
            print(f'{pos_menores[n]}', end=', ')
        elif n < len(pos_menores) - 1:
            print(f'{pos_menores[n]}', end=' e ')
        else:
            print(f'{pos_menores[n]}')


# RESOLUÇÃO GUANABARA
'''lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print("-="*30)
print(f"Você digitou os valores {lista}")
print(f"O maior valor é {maior} e ele está nas posições ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}... ", end='')
print()
print(f"O menor valor é {menor} e ele está nas posições ", end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}... ", end='')
print()
'''