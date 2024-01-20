# DESAFIO 73
# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO
# CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
# OS 5 PRIMEIROS TIMES
# OS ÚLTIMOS 4 COLOCADOS
# TIMES EM ORDEM ALFABÉTICA
# EM QUE POSIÇÃO ESTÁ O TIME DO FLAMENGO

# MINHA RESOLUÇÃO
'''times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')

print('-=' * 20)
print('Lista de times do Brasileirão (por ordem de classificação):')
print(times)
print('-=' * 20)
print('Os 5 primeiros colocados são: ', end='')
print(times[0:5])
print('-=' * 20)
print(f'Os 4 últimos são: ', end='')
print(times[-4:])
print('-=' * 20)
print('Times em ordem alfabética: ', end='')
print(sorted(times))
print('-=' * 20)
print(f'O FLAMENGO está na {times.index("Flamengo") + 1}ª posição')'''

# MINHA RESOLUÇÃO FODA
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')

print(f'{" TABELA DO CAMPEONATO BRASILEIRO 2023 ":=^80}')
while True:
    print('''\n---- MENU DE OPÇÕES ----
[1] CLASSIFICAÇÃO
[2] 5 PRIMEIROS COLOCADOS
[3] 4 ÚLTIMOS COLOCADOS
[4] TIMES EM ORDEM ALFABÉTICA
[5] POSIÇÃO DO MENGÃO
[6] SAIR''')
    op = int(input('\nDigite o número da opção desejada: '))
    if op == 1:
        print()
        print('-=' * 20)
        print('CLASSIFICAÇÃO DO CAMPEONATO BRASILEIRO:')
        for posi, time in enumerate(times):
            print(posi + 1, time)
        print('-=' * 20)
    elif op == 2:
        print()
        print('-=' * 20)
        print('OS 5 PRIMEIROS COLOCADOS SÃO:')
        for posi in range(0, 5):
            print(posi + 1, times[posi])
        print('-=' * 20)
    elif op == 3:
        print()
        print('-=' * 20)
        print(f'OS 4 ÚLTIMOS COLOCADOS SÃO:')
        for posi in range(16, 20):
            print(posi + 1, times[posi])
        print('-=' * 20)
    elif op == 4:
        print()
        print('-=' * 20)
        print('TIMES EM ORDEM ALFABÉTICA:')
        alfabetica = sorted(times)
        for time in alfabetica:
            print(time)
        print('-=' * 20)
    elif op == 5:
        print()
        print('-=' * 20)
        print(f'O FLAMENGO ESTÁ {times.index("Flamengo") + 1}ª POSIÇÃO')
        print('-=' * 20)
    elif op == 6:
        break
    else:
        print()
        print('-=' * 20)
        print('OPÇÃO INVÁLIDA')
        print('-=' * 20)

print('Você saiu do programa')
