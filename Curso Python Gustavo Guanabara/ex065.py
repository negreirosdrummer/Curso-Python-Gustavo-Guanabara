# DESAFIO 65
# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
# NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS.
# O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES

# MINHA RESOLUÇÃO
continuar = ' '
soma = cont = maior = menor = 0
while continuar != 'N':
    continuar = ' '
    num = int(input('Digite um número inteiro: '))
    if cont == 0:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    cont += 1
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
media = soma / cont
print(f'\nForam digitados {cont} valores')
print(f'A média entre eles é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')


# RESOLUÇÃO GUANABARA
"""
continuar = 'S'
soma = cont = maior = menor = 0
while continuar in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
media = soma / cont
print(f'\nForam digitados {cont} valores')
print(f'A média entre eles é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
"""