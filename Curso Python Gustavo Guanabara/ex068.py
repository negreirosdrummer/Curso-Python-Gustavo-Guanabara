# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR.
# O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O
# TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.

# MINHA RESOLUÇÃO
from random import randint

print('-=' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 12)
ganhou = True
cont = 0
while ganhou:
    num = int(input('Digite um valor: '))
    par_impar = input('Par ou Ímpar? [P/I] ').strip().upper()
    while par_impar not in 'PI':
        par_impar = input('Entrada inválida! Digite somente P ou I: ').strip().upper()
    pc = randint(0, 10)
    soma = num + pc
    if soma % 2 == 0:
        resultado = 'PAR'
    elif soma % 2 == 1:
        resultado = 'ÍMPAR'
    print('----' * 15)
    print(f'Você jogou {num} e o computador jogou {pc}. A soma deu {soma} ({resultado})')
    print('----' * 15)

    if par_impar == 'P' and soma % 2 == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        ganhou = True
        cont += 1
    elif par_impar == 'I' and soma % 2 == 1:
        print('Você GANHOU!')
        ganhou = True
        cont += 1
    else:
        print('Você PERDEU!')
        ganhou = False

print('-=' * 15)
if cont == 0:
    print(f'GAME OVER! Você não venceu nenhuma vez')
elif cont == 1:
    print(f'GAME OVER! Você venceu {cont} vez')
else:
    print(f'GAME OVER! Você venceu {cont} vezes')


# RESOLUÇÃO GUANABARA
'''from random import randint

print('-=' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 12)
cont = 0
while True:
    num = int(input('Digite um valor: '))
    pc = randint(0, 10)
    soma = num + pc
    par_impar = input('Par ou Ímpar? [P/I] ').strip().upper()
    while par_impar not in 'PI':
        par_impar = input('Entrada inválida! Digite somente P ou I: ').strip().upper()
    print('----' * 15)
    print(f'Você jogou {num} e o computador jogou {pc}. A soma deu {soma} ', end='')
    print('(PAR)' if soma % 2 == 0 else '(ÍMPAR)')
    print('----' * 15)

    if par_impar == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif par_impar == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')

print('-=' * 15)
if cont == 0:
    print(f'GAME OVER! Você não venceu nenhuma vez')
elif cont == 1:
    print(f'GAME OVER! Você venceu {cont} vez')
else:
    print(f'GAME OVER! Você venceu {cont} vezes')'''
