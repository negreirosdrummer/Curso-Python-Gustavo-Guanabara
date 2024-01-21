# DESAFIO 30
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR

num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar')

# usando condição simplificada:
# print(f'O número {num} é par!' if num % 2 == 0 else f'O número {num} é ímpar')
