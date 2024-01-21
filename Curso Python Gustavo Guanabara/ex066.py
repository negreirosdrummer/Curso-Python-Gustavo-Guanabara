# DESAFIO 66
# CRIE UM PROGRAMA QUE LEIA NÚMEROS INTEIROS PELO TECLADO.
# O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA.
# NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELAS (DESCONSIDERANDO O FLAG)

# MINHA RESOLUÇÃO
soma = cont = 0
while True:
    num = int(input('Digite um número inteiro (999 para sair): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'\nForam digitados {cont} valores.')
print(f'A soma dos valores resulta em {soma}')

# RESOLUÇÃO GUANABARA: A MINHA ESTÁ IGUAL
