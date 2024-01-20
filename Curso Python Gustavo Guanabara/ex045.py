# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ

from random import randint
from time import sleep

print('-=' * 11)
print('PEDRA PAPEL E TESOURA')
print('-=' * 11)
lista = ['Pedra', 'Papel', 'Tesoura']
print("""
1 - PEDRA
2 - PAPEL
3 - TESOURA
""")

jogador = int(input('Digite o número da opção desejada: ')) - 1
pc = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!\n')

print('-=' * 13)
print(f'Você escolheu {lista[jogador]}')
print(f'O computador escolheu {lista[pc]}')
print('-=' * 13)
if jogador == pc:
    print('\nEMPATE!')
elif jogador == 0 and pc == 2:
    print('\n\033[1;32mVOCÊ GANHOU!')
elif jogador == 1 and pc == 0:
    print('\n\033[1;32mVOCÊ GANHOU!')
elif jogador == 2 and pc == 1:
    print('\n\033[1;32mVOCÊ GANHOU!')
else:
    print('\n\033[1;31mVOCÊ PERDEU!')
