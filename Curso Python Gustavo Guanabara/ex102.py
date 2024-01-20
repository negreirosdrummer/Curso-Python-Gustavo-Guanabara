# DESAFIO 102
# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS:
# O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO (OPCIONAL) INDICANDO SE
# SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL

# MINHA RESOLUÇÃO
from time import sleep


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um número 'n'
    """
    fatorial = num
    i = num
    if not show:
        while num > 1:
            fatorial *= num - 1
            num -= 1
        print(f'{i}! = {fatorial}')
    else:
        print(f'{i}!', end='')
        sleep(0.25)
        print(' = ', end='')
        sleep(0.25)
        while num > 1:
            print(num, end='')
            sleep(0.25)
            print(' x ', end='')
            sleep(0.25)
            fatorial *= num - 1
            num -= 1
        if num == 1:
            print(num, end='')
            sleep(0.25)
            print(' = ', end='')
            sleep(0.25)
            fatorial *= num

        print(f'{fatorial}')


num = int(input('Digite um número: '))
show = input('Deseja mostrar o cálculo do fatorial? [S/N] ').strip().upper()
while show not in 'SN':
    show = input('Mostrar o cálculo do fatorial? (Digite somente S ou N): ').strip().upper()

if show == 'S':
    show = True
elif show == 'N':
    show = False

fatorial(num, show)


# RESOLUÇÃO GUANABARA

# def fatorial(n, show=False):
#     """
#         -> Calcula o fatorial de um número.
#         :param n: número a ser calculado
#         :param show: (opcional) mostrar ou não a conta
#         :return: o valor do fatorial de um número 'n'
#     """
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f *= c
#     return f


# print(fatorial(5, show=True))
# help(fatorial)
