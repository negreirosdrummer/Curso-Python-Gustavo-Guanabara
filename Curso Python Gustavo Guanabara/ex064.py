# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
# O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA.
# NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG)

# MINHA RESOLUÇÃO
num = soma = cont = 0
while num != 999:
    soma += num
    num = int(input('Digite um número inteiro (999 para sair): '))
    if num != 999:
        cont += 1
print(f'\nForam digitados {cont} valores.')
print(f'A soma dos valores resulta em {soma}')

# RESOLUÇÃO GUANABARA
soma = cont = 0
# a diferença está nessa linha (está antes do laço while para que o valor inserido não seja contabilizado na contagem)
num = int(input('Digite um número inteiro (999 para sair): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número inteiro (999 para sair): '))
print(f'\nForam digitados {cont} valores.')
print(f'A soma dos valores resulta em {soma}')
