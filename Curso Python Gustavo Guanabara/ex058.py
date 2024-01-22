# DESAFIO 58
# MELHORE O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI "PENSAR" EM UM NÚMERO ENTRE 0 E 10.
# SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO
# FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER

from random import randint

# MINHA RESOLUÇÃO:
print('-=-' * 17)
print('Vou pensar em um número de 0 a 10. Tente adivinhar!')
print('-=-' * 17)
numero = randint(0, 10)
palpite = ' '
cont = 0
while palpite != numero:
    palpite = int(input('Em que número eu pensei? '))
    cont += 1
    if palpite > numero:
        print('Menos... Tente novamente\n')
    elif palpite < numero:
        print('Mais... Tente novamente\n')

print('\nPARABÉNS! Você acertou!')
print(f'Foram necessárias {cont} tentativas.')


# RESOLUÇÃO GUANABARA (a única diferença é a condição do laço while)
"""
print('-=-' * 17)
print('Vou pensar em um número de 0 a 10. Tente adivinhar!')
print('-=-' * 17)
numero = randint(0, 10)
acertou = False
cont = 0
while not acertou:
    palpite = int(input('Em que número eu pensei? '))
    cont += 1
    if palpite == numero:
        acertou = True
    else:
        if palpite > numero:
            print('Menos... Tente novamente\n')
        elif palpite < numero:
            print('Mais... Tente novamente\n')

print('\nPARABÉNS! Você acertou!')
print(f'Foram necessárias {cont} tentativas.')
"""