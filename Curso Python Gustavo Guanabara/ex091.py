# DESAFIO 91
# CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS.
# GUARDE ESSES RESULTADOS EM UM DICIONÁRIO EM PYTHON.
# NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO

# MINHA RESOLUÇÃO
from random import randint
from time import sleep
from operator import itemgetter

dict_jogadores = {}
print('Valores sorteados:')
for c in range(4):
    num = randint(1, 6)
    print(f'\tO Jogador{c + 1} tirou {num}')
    dict_jogadores[c + 1] = num
    sleep(0.5)

# o itemgetter(1) organiza o dicionário pelos valores
# se fosse itemgetter(0), organizaria pelas chaves
dict_ordenado = sorted(dict_jogadores.items(), key=itemgetter(1), reverse=True)
print(f'\n{"== RANKING DOS JOGADORES ==":^32}')
for i, v in enumerate(dict_ordenado):
    print(f'\t{i + 1}º Lugar: Jogador{v[0]} que tirou {v[1]} no dado')


# RESOLUÇÃO GUANABARA
"""
from random import randint
from time import sleep
from operator import itemgetter

jogo = {"Jogador1": randint(1, 6),
        "Jogador2": randint(1, 6),
        "Jogador3": randint(1, 6),
        "Jogador4": randint(1, 6)
        }
ranking = list()
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("-=" * 30)
print("   == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f"    {i+1}º Lugar: {v[0]} com {v[1]}.")
"""
