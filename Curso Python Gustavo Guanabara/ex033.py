# DESAFIO 33
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite mais um número: '))
maior = num1
menor = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print(f'Os úmeros digitados foram {num1}, {num2} e {num3}')
print(f'O maior é {maior}')
print(f'O menor é {menor}')
