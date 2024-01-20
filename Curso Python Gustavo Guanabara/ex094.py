# CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE
# CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA.
# NO FINAL, MOSTRE:
# QUANTAS PESSOAS FORAM CADASTRADAS
# A MÉDIA DE IDADE
# UMA LISTA COM AS MULHERES
# UMA LISTA DE PESSOAS COM IDADE ACIMA DA MÉDIA

# MINHA RESOLUÇÃO
lista = []
pessoa = {}
mulheres = []
idade_acima_media = []
soma_idades = media_idades = 0
while True:
    pessoa['nome'] = input('Nome: ')
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        sexo = input('Sexo (Digite somente M ou F): ').strip().upper()
    pessoa['sexo'] = sexo
    if sexo == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    soma_idades += pessoa['idade']
    lista.append(pessoa.copy())
    continuar = input('Cadastrar mais uma pessoa? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Cadastrar mais uma pessoa? Digite somente S ou N: ').strip().upper()
    if continuar == 'N':
        break

media_idades = soma_idades / len(lista)
print('-=' * 20)
print(f'Pessoas cadastradas: {len(lista)}')
print(f'Média de idade do grupo: {media_idades:.2f}')
if len(mulheres) > 0:
    print(f'As mulheres cadastradas foram: ', end='')
    cont_m = len(mulheres)
    for i in mulheres:
        if cont_m > 2:
            print(i, end=', ')
            cont_m -= 1
        elif cont_m == 2:
            print(i, end=' e ')
            cont_m -= 1
        else:
            print(i)
else:
    print('Nenhuma mulher foi cadastrada!')

if len(lista) > 1:
    print('Lista das pessoas com idade acima da média:\n')
    for i in lista:
        for k, v in i.items():
            if i['idade'] > media_idades:
                if k == 'idade':
                    print(f'{k} = {v}')
                else:
                    print(f'{k} = {v}', end='; ')
    print()
else:
    print()
print('<<<< ENCERRADO >>>>')


# MINHA RESOLUÇÃO ANTIGA
'''lista_pessoas = []
pessoa = {}
soma_idades = 0
while True:
    pessoa["Nome"] = str(input("Nome: "))
    pessoa["Sexo"] = str(input("Sexo: [M/F] ")).upper()  # poderia usar .upper()[0] para pegar só a primeira letra
    while pessoa["Sexo"] not in "MF":
        print("ERRO! Digite apenas M ou F")
        pessoa["Sexo"] = str(input("Sexo: [M/F] ")).upper()  # poderia usar .upper()[0] para pegar só a primeira letra
    pessoa["Idade"] = int(input("Idade: "))
    soma_idades += pessoa["Idade"]
    lista_pessoas.append(pessoa.copy())
    resp = str(input("Quer continuar? [S/N] "))
    while resp not in 'SsNn':
        print("ERRO! Responda apenas S ou N")
        resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break

media_idades = soma_idades / len(lista_pessoas)
print("-=" * 30)
print(lista_pessoas)
print(f"Foram cadastradas {len(lista_pessoas)} pessoas.")
print(f"A média de idades é de {media_idades} anos.")  # poderia colocar {media_idades:5.2f}
mulheres = []
acima_da_media = []
for i in range(len(lista_pessoas)):
    for k, v in lista_pessoas[i].items():
        if v == 'F':
            mulheres.append(lista_pessoas[i]["Nome"])
    if lista_pessoas[i]["Idade"] > media_idades:
        acima_da_media.append(lista_pessoas[i])

print(f"As mulheres cadastradas foram: ")
for i in range(len(mulheres)):
    if i == len(mulheres)-2:
        print(f"{mulheres[i]}", end=" e ")
    elif i == len(mulheres)-1:
        print(f"{mulheres[i]}.")
    else:
        print(f"{mulheres[i]}", end=", ")
print(f"Lista de pessoas com idade acima da media:")

for i in range(len(acima_da_media)):
    for k, v in acima_da_media[i].items():
        print(f"{k}", end=' = ')
        print(f"{v}", end='; ')
    print()
print("<< ENCERRADO >>")'''


# RESOLUÇÃO GUANABARA
'''galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("ERRO! Digite apenas M ou F")
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SsNn':
            break
        print("ERRO! Responda apenas S ou N")
    if resp == 'N':
        break

print('-=' * 30)
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"A média de idades é de {media:5.2f} anos.")
mulheres = []
acima_da_media = []
for p in galera:
    if p["Sexo"] == 'F':
        mulheres.append(p["Nome"])
    if p["Idade"] > media:
        acima_da_media.append(p)

print(f"As mulheres cadastradas foram: ")
for i in range(len(mulheres)):
    if i == len(mulheres)-2:
        print(f"{mulheres[i]}", end=" e ")
    elif i == len(mulheres)-1:
        print(f"{mulheres[i]}.")
    else:
        print(f"{mulheres[i]}", end=", ")
print(f"Lista de pessoas com idade acima da media:")

for i in range(len(acima_da_media)):
    for k, v in acima_da_media[i].items():
        print(f"{k}", end=' = ')
        print(f"{v}", end='; ')
    print()
print("<< ENCERRADO >>")'''
