# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO TENTAR
# DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU

from random import randint
from time import sleep

print('-=-' * 19)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 19)
numero = randint(0, 5)
palpite = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(0.5)
if palpite == numero:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numero}, e não no {palpite}!')

# usando condição simplificada:
# print('Você acertou!!' if palpite == numero else 'Você errou...')
