# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARÂMETROS OPCIONAIS:
# O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.
# O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE

# MINHA RESOLUÇÃO

def ficha(nome='<desconhecido>', gols=0):
    if gols > 1:
        print(f'O jogador {nome} fez {gols} gols no campeonato')
    elif gols == 1:
        print(f'O jogador {nome} fez {gols} gol no campeonato')
    elif gols == 0:
        print(f'O jogador {nome} não marcou gols no campeonato')


nome = input('Nome do jogador: ')
try:
    gols = int(input('Número de gols: '))
except ValueError:
    gols = 0

if nome == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)


# RESOLUÇÃO GUANABARA

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
