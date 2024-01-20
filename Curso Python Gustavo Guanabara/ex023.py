# DESAFIO 23
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS

num = int(input('Digite um número de 0 a 9999: '))
un = num // 1 % 10
dz = num // 10 % 10
cn = num // 100 % 10
mi = num // 1000 % 10

print(f'unidade: {un}')
print(f'dezena: {dz}')
print(f'centena: {cn}')
print(f'milhar: {mi}')
