# DESAFIO 84
# FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
# QUANTAS PESSOAS FORAM CADASTRADAS
# UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
# UMA LISTAGEM COM AS PESSOAS MAIS LEVES

# MINHA RESOLUÇÃO
pessoa = []
todos = []
maior_peso = menor_peso = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso (Kg): ')))
    if len(todos) == 0:
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] >= maior_peso:
            maior_peso = pessoa[1]
        elif pessoa[1] <= menor_peso:
            menor_peso = pessoa[1]
    todos.append(pessoa[:])
    pessoa.clear()
    continuar = input('Continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Digite somente S ou N: ').strip().upper()
    if continuar == 'N':
        break
print('-=' * 20)
print(f'{len(todos)} pessoas foram cadastradas')
mais_pesados = []
mais_leves = []

for i in range(len(todos)):
    if todos[i][1] == maior_peso:
        mais_pesados.append(todos[i][0])
    elif todos[i][1] == menor_peso:
        mais_leves.append(todos[i][0])

cont_p = len(mais_pesados)
if cont_p == 1:
    print(f'O maior peso foi {maior_peso} Kg. Peso de {mais_pesados[0]}')
elif cont_p > 1:
    print(f'O maior peso foi {maior_peso} Kg. Peso de ', end='')
    for p in range(len(mais_pesados)):
        if cont_p > 2:
            print(mais_pesados[p], end=', ')
            cont_p -= 1
        elif cont_p == 2:
            print(mais_pesados[p], end=' e ')
            cont_p -= 1
        else:
            print(mais_pesados[p])

cont_l = len(mais_pesados)
if cont_l == 1:
    print(f'O menor peso foi {menor_peso} Kg. Peso de {mais_leves[0]}')
elif cont_l > 1:
    print(f'O menor peso foi {menor_peso} Kg. Peso de ', end='')
    for p in range(len(mais_leves)):
        if cont_l > 2:
            print(mais_leves[p], end=', ')
            cont_l -= 1
        elif cont_l == 2:
            print(mais_leves[p], end=' e ')
            cont_l -= 1
        else:
            print(mais_leves[p])


# RESOLUÇÃO GUANABARA
"""
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso (kg): ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = input("Deseja continuar? [S/N] ")
    while resp not in "NnSs":
        resp = input("Deseja continuar? [S/N] ")
    if resp in "Nn":
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} Kg. Peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f' [{p[0]}]', end='')
print()
print(f'O menor peso foi de {men} Kg. Peso de', end='')
for p in princ:
    if p[1] == men:
        print(f' [{p[0]}]', end='')
"""
