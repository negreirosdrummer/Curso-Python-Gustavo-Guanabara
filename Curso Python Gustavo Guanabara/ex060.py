# DESAFIO 60
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL. EXEMPLO:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# MINHA RESOLUÇÃO USANDO WHILE
from time import sleep
num_inicial = fatorial = cont = int(input('Digite um número inteiro: '))

while cont != 1:
    fatorial *= cont - 1
    print(f'{cont}', end='')
    sleep(0.25)
    print(' x ', end='')
    sleep(0.25)
    cont -= 1
print(f'{cont}', end='')
sleep(0.25)
print(f' = ', end='')
sleep(0.25)
print(fatorial)
sleep(1)

print(f'\n{num_inicial}! = {fatorial}')


# MINHA RESOLUÇÃO USANDO FOR
for c in range(num_inicial - 1, 1, -1):
    fatorial *= c
print(f'{num_inicial}! = {fatorial}')


# RESOLUÇÃO GUANABARA USANDO O MÓDULO FACTORIAL
from math import factorial
num = int(input('Digite um número inteiro: '))
print(f'{num}! = {factorial(num)}')


# RESOLUÇÃO GUANABARA USANDO WHILE
n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')


# RESOLUÇÃO GUANABARA USANDO FOR
n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}')
