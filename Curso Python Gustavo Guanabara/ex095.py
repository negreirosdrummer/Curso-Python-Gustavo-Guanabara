# APRIMORE O DESAFIO 93 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM
# SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR

# MINHA RESOLUÇÃO
'''jogadores = []
jogador = {}
total_gols = 0

while True:
    jogador['Nome'] = input('Nome: ')
    jogador['Partidas'] = int(input('Partidas: '))
    jogador['Gols'] = []
    total_gols = 0
    for c in range(jogador['Partidas']):
        gol = int(input(f'Gols na partida {c + 1}: '))
        jogador['Gols'].append(gol)
        total_gols += gol
    jogador['Total'] = total_gols
    jogadores.append(jogador.copy())
    continuar = input('Inserir mais um jogador? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Inserir mais um jogador? (Digite somente S ou N): ').strip().upper()
    if continuar == 'N':
        print('-=' * 25)
        break
    print('--' * 25)

print(f'{"id":<5}{"Nome":<20}{"Gols":<20}{"Total"}')
print('--' * 25)
for i in range(len(jogadores)):
    print(f'{i:<5}', end='')
    print(f'{jogadores[i]["Nome"]:<20}', end='')
    print(f'{str(jogadores[i]["Gols"]):<20}', end='')
    print(f'{jogadores[i]["Total"]}', end='')
    print()
print('-=' * 25)
while True:
    id = int(input('Digite o id de um jogador para visualizar detalhes (999 para sair): '))
    if id == 999:
        break
    elif id > len(jogadores) - 1 or id < 0:
        print(f'Erro! Não existe jogador com ID {id}')
    else:
        print(f'-- Levantamento do jogador {jogadores[id]["Nome"]}')
        for i in range(jogadores[id]['Partidas']):
            if jogadores[id]["Gols"][i] == 0:
                print(f'\t=> Na partida {i + 1} não marcou gols')

            elif jogadores[id]["Gols"][i] == 1:
                print(f'\t=> Na partida {i + 1} fez {jogadores[id]["Gols"][i]} gol')
            else:
                print(f'\t=> Na partida {i + 1} fez {jogadores[id]["Gols"][i]} gols')
    print('-=' * 25)
print('<< VOLTE SEMPRE >>')'''


# RESOLUÇÃO GUANABARA
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome: "))
    tot = int(input(f"Quantas partidas o jogador {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c+1}: ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N")
    if resp == 'N':
        break

print("-=" * 30)
print("cod ", end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-"*40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-"*40)

while True:
    cod = int(input("Mostrar dados de qual jogador? (999 para sair) "))
    if cod == 999:
        break
    elif cod < 0 or cod >= len(time):
        print(f"Erro! Não existe jogador com o código {cod}")
    else:
        print(f"-- Levantamento do jogador {time[cod]['nome']}:")
        for k, v in enumerate(time[cod]["gols"]):
            print(f"\tNo jogo {k+1}, fez {v} gols.")
    print("-" * 40)
print("<< VOLTE SEMPRE >>")
