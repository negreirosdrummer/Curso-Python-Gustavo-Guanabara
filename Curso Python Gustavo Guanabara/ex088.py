# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES.
# O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE
# 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA.

# MINHA RESOLUÇÃO
from random import randint
from time import sleep

lista_jogos = []
print(f'{" GERADOR DE JOGOS DA MEGA-SENA ":-^40}')
qtd_jogos = int(input('Quantos jogos deseja gerar? '))
for i in range(qtd_jogos):
    jogo = []
    lista_jogos.append(jogo)

print(f'\n-=-=-= GERANDO {qtd_jogos} JOGOS =-=-=-')
for i in range(len(lista_jogos)):
    while len(lista_jogos[i]) < 6:
        num = randint(1, 60)
        if num not in lista_jogos[i]:
            lista_jogos[i].append(num)
    lista_jogos[i].sort()
    print(f'Jogo {i + 1}: {lista_jogos[i]}')
    sleep(0.5)

print('-=-=-= < BOA SORTE! > =-=-=-')


# MINHA RESOLUÇÃO ANTIGA
'''from random import randint
from time import sleep

lista = []
jogo = []
print("-"*30)
print("JOGO NA MEGA SENA")
print("-"*30)
qtd_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"\n-=-=-=  SORTEANDO {qtd_jogos} JOGOS  =-=-=-")
for c in range(qtd_jogos):
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        else:
            continue
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()

for i in range(len(lista)):
    print(f'Jogo {i + 1}: {lista[i]}')
    sleep(0.5)

print('-=' * 4, ' < BOA SORTE! > ', '=-'*4)'''

# RESOLUÇÃO GUANABARA
'''from random import randint
from time import sleep

lista = []
jogos = []
print("-"*30)
print("      JOGA NA MEGA SENA")
print("-"*30)
qtd_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
total = 1
while total <= qtd_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f'SORTEANDO {qtd_jogos} JOGOS', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)

print('-=' * 3, ' << BOA SORTE! >> ', '=-' * 3)'''
