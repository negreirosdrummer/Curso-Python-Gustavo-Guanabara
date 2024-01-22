# DESAFIO 106
#

# MINHA RESOLUÇÃO
"""
from time import sleep


def func(lib):
    tam = len(lib) + 36
    print()
    print(f'\033[44m{"~"}' * tam)
    print(f"  Acessando o manual do comando '{lib}'")
    print('~' * tam)
    sleep(1)
    print('\033[m')
    print('\033[7m')
    help(lib)
    print('\033[m')
    sleep(1)


while True:
    print(f'\033[42m{"~~"}' * 15)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('~~' * 15)
    lib = input('\033[m\nFunção ou biblioteca: ')
    if lib == 'fim':
        break
    else:
        func(lib)
print()
print(f"\033[41m{'~'}" * 13)
print('  ATÉ LOGO!')
print('~' * 13)
"""


# RESOLUÇÃO GUANABARA

from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[5], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO', 1)
