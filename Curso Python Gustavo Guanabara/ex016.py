# DESAFIO 16
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
# Ex.: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

from math import floor
num = float(input('Digite um número real: '))
print(f'O número {num} tem a parte inteira {floor(num)}')  # poderia usar math.trunc(num) também

# poderia fazer dessa forma também:
print(f'O número {num} tem a parte inteira {num:.0f}')

# outra forma:
print(f'O número {num} tem a parte inteira {int(num)}')
