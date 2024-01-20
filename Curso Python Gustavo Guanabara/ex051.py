# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA.
# NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

print('==' * 15)
print(f'{"10 TERMOS DE UMA P.A.":^30}')
print('==' * 15)
inicio = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))

# MINHA RESOLUÇÃO:
# soma = inicio
# for c in range(1, 10):
#     print(f'{soma}', end='\033[33m -> \033[m')
#     soma += razao
    # checa se é o último número da P.A. para não imprimir a seta depois dele
#     if c == 9:
#         print(soma)
# poderia retirar o 'if' acima e imprimir a palavra 'acabou' depois da última seta
# print('\033[1;32mACABOU!')

# RESOLUÇÃO GUANABARA:
# calcula o décimo termo da P.A.
decimo = inicio + (10 - 1) * razao
for c in range(inicio, decimo + razao, razao):
    print(f'{c}', end='\033[33m -> \033[m')
print('\033[1;32mACABOU!')
