# DESAFIO 74
# CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA.
# DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA

# MINHA RESOLUÇÃO
'''from random import randint
lista = []
for c in range(5):
    num = randint(0, 10)
    lista.append(num)
tupla = tuple(lista)
print('Os números sorteados foram ', end='')
for n in range(len(tupla)):
    if n < len(tupla) - 2:
        print(tupla[n], end=', ')
    elif n < len(tupla) - 1:
        print(tupla[n], end=' e ')
    else:
        print(tupla[n])
for n in range(len(tupla)):
    if n == 0:
        maior = menor = tupla[n]
    else:
        if tupla[n] > maior:
            maior = tupla[n]
        elif tupla[n] < menor:
            menor = tupla[n]

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')'''

# RESOLUÇÃO GUANABARA
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), )
print('Os números sorteados foram:', end='')
for n in numeros:
    print(f' {n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
