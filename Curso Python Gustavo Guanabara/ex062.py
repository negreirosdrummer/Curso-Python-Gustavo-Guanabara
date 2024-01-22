# DESAFIO 62
# MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS.
# O PROGRAMA ENCERRARÁ QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS

# MINHA RESOLUÇÃO
"""
print('==' * 15)
print(f'{"10 TERMOS DE UMA P.A.":^30}')
print('==' * 15)
inicio = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))

soma = inicio
cont = 0
while cont < 10:
    print(f'{soma}', end='\033[33m -> \033[m')
    soma += razao
    cont += 1
print('\033[1;32mPAUSA\033[m')

termos_adicionais = 1
while termos_adicionais != 0:
    termos_adicionais = int(input('\nDeseja exibir quantos termos adicionais? (0 para finalizar): '))
    cont = 0
    while cont < termos_adicionais:
        print(f'{soma}', end='\033[33m -> \033[m')
        soma += razao
        cont += 1
    if termos_adicionais != 0:
        print('\033[1;32mPAUSA\033[m')
print('\033[1;32mACABOU!!\033[m')
"""


# RESOLUÇÃO GUANABARA:
print('==' * 15)
print(f'{"10 TERMOS DE UMA P.A.":^30}')
print('==' * 15)
primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))
termo = primeiro
cont = 1
total = 0
termos_adicionais = 10
while termos_adicionais != 0:
    total += termos_adicionais
    while cont <= total:
        print(f'{termo}', end='\033[33m -> \033[m')
        termo += razao
        cont += 1
    print('\033[1;32mPAUSA\033[m')
    termos_adicionais = int(input('\nDeseja exibir quantos termos adicionais? (0 para finalizar): '))
print('\033[1;32mACABOU!!\033[m')
print(f'Progressão finalizada com {total} termos')
