# CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL.
# O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU.
# DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA.
# NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO

# MINHA RESOLUÇÃO
jogador = dict()
total_gols = 0
jogador['Nome'] = input('Nome: ')
qtd_partidas = int(input('Partidas: '))
jogador['Gols'] = []
for c in range(qtd_partidas):
    gol = int(input(f'Gols na partida {c + 1}: '))
    jogador['Gols'].append(gol)
    total_gols += gol

jogador['Total'] = total_gols
print('-=' * 20)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 20)
print(f'O jogador {jogador["Nome"]} jogou {qtd_partidas} partidas')
for i in range(qtd_partidas):
    if jogador["Gols"][i] == 0:
        print(f'\t=> Na partida {i + 1} não marcou gols')

    elif jogador["Gols"][i] == 1:
        print(f'\t=> Na partida {i + 1} fez {jogador["Gols"][i]} gol')
    else:
        print(f'\t=> Na partida {i + 1} fez {jogador["Gols"][i]} gols')
print(f'Foi um total de {jogador["Total"]} gols em {qtd_partidas} partidas')


# MINHA RESOLUÇÃO ANTIGA
'''jogador = {}
jogador["Nome"] = str(input("Nome: "))
jogador["Partidas"] = int(input("Partidas: "))
lista_gols = []
for c in range(jogador["Partidas"]):
    gols = int(input(f"Digite quantos gols esse jogador marcou na partida {c+1}: "))
    lista_gols.append(gols)
    # poderia ter resumido: lista_gols.append(int(input(f"Digite quantos gols esse jogador marcou na partida {c+1}: ")))

jogador["Gols Marcados"] = lista_gols  # seria melhor: lista_gols[:]
total = 0
for g in lista_gols:
    total += g

jogador["Total de Gols"] = total

print()
print("-="*30)
print(jogador)
print("-="*30)
for k, v in jogador.items():
    print(f"{k}: {v}")
print("-="*30)
print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas.")

for k, v in enumerate(jogador["Gols Marcados"]):
    print(f"\t=> Na partida {k+1}, fez {v} gols.")
print(f"Foi um total de {jogador['Total de Gols']} gols.")'''


# RESOLUÇÃO GUANABARA
'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')'''
