# DESAFIO 71
# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO.
# NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO) E
# O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.
# OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$ 50, R$ 20, R$ 10 E R$ 1

# MINHA RESOLUÇÃO
"""
print('==' * 25)
print(f'{"BANCO NEGREIROS":^50}')
print('==' * 25)

sacar = resto = int(input('\nDigite o valor do saque: R$ '))

if resto >= 50:
    cedula_50 = resto // 50
    resto = resto - (cedula_50 * 50)
    if cedula_50 == 1:
        print(f'\nTotal de {cedula_50} cédula de R$ 50')
    else:
        print(f'\nTotal de {cedula_50} cédulas de R$ 50')

if resto >= 20:
    cedula_20 = resto // 20
    resto = resto - (cedula_20 * 20)
    if cedula_20 == 1:
        print(f'Total de {cedula_20} cédula de R$ 20')
    else:
        print(f'Total de {cedula_20} cédulas de R$ 20')

if resto >= 10:
    cedula_10 = resto // 10
    resto = resto - (cedula_10 * 10)
    if cedula_10 == 1:
        print(f'Total de {cedula_10} cédula de R$ 10')
    else:
        print(f'Total de {cedula_10} cédulas de R$ 10')

if resto >= 1:
    cedula_1 = resto // 1
    resto = resto - (cedula_1 * 1)
    if cedula_1 == 1:
        print(f'Total de {cedula_1} cédula de R$ 1')
    else:
        print(f'Total de {cedula_1} cédulas de R$ 1')

print()
print('==' * 25)
print(f'Volte sempre ao BANCO NEGREIROS! Tenha um bom dia!')
"""


# RESOLUÇÃO GUANABARA
print('==' * 25)
print(f'{"BANCO CEV":^50}')
print('==' * 25)

valor = int(input('\nDigite o valor do saque: R$ '))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print()
print('==' * 25)
print(f'Volte sempre ao BANCO CEV! Tenha um bom dia!')
