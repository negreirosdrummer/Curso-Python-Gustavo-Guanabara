# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR().
# A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI
# MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR

# MINHA RESOLUÇÃO
from random import randint
from time import sleep


def sorteia():
    lista = list()
    print(f'Sorteando 5 valores: ', end='')
    for c in range(5):
        num = randint(0, 10)
        lista.append(num)
        print(num, end='... ')
        sleep(0.25)
    print('PRONTO!')
    return lista


def soma_par(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares da lista {lista}, temos {soma}')


sorteia = sorteia()
soma_par(sorteia)


# RESOLUÇÃO GUANABARA
'''from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.25)
    print('PRONTO!')


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
soma_par(numeros)'''
