# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
# SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR   

# MINHA RESOLUÇÃO
from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.25)
    if len(num) > 1:
        print(f'\nForam informados {len(num)} valores ao todo')
    elif len(num) == 1:
        print(f'\nFoi informado somente {len(num)} valor')
    elif len(num) == 0:
        print('\nNenhum valor foi informado')
    for c in range(len(num)):
        if c == 0:
            maior = num[0]
        else:
            if num[c] > maior:
                maior = num[c]

    print(f'O maior valor informado foi {maior}' if len(num) > 0 else '')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


# RESOLUÇÃO GUANABARA
'''from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''
