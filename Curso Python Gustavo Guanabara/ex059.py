# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] MAIOR
# [ 4 ] NOVOS NÚMEROS
# [ 5 ] SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO

from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
op = 0

while op != 5:
    print()
    print('-=' * 7)
    print('MENU DE OPÇÕES')
    print('-=' * 7)
    print("""[1] SOMA
[2] MULTIPLICAÇÃO
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA""")

    op = int(input('\nDigite a opção desejada: '))

    if op == 1:
        print(f'A soma dos números {num1} e {num2} é igual a {num1 + num2}')
    elif op == 2:
        print(f'O produto dos números {num1} e {num2} é igual a {num1 * num2}')
    elif op == 3:
        if num1 > num2:
            print(f'O maior entre {num1} e {num2} é {num1}')
        elif num2 > num1:
            print(f'O maior entre {num1} e {num2} é {num2}')
    elif op == 4:
        print('Informe os números novamente')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif op == 5:
        print('Finalizando...')
        print('-=' * 7)
    else:
        print('Opção inválida! Tente novamente')
    sleep(1)
