# DESAFIO 61
# REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS
# 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE

# MINHA RESOLUÇÃO:
print('==' * 15)
print(f'{"10 TERMOS DE UMA P.A.":^30}')
print('==' * 15)
inicio = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))

soma = inicio
cont = 0
while cont < 10:
    if cont != 9:
        print(f'{soma}', end='\033[33m -> \033[m')
    elif cont == 9:
        print(soma)
    soma += razao
    cont += 1
print('\033[1;32mACABOU!\033[m')


# RESOLUÇÃO GUANABARA:
"""
print('==' * 15)
print(f'{"10 TERMOS DE UMA P.A.":^30}')
print('==' * 15)
inicio = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))

print('==' * 15)
print(f'{"10 TERMOS DE UMA P.A.":^30}')
print('==' * 15)
primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{soma}', end='\033[33m -> \033[m')
    termo += razao
    cont += 1
print('\033[1;32mACABOU!\033[m')
"""
