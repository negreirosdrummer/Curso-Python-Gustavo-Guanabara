# DESAFIO 24
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"

# MINHA RESOLUÇÃO
cidade = input('Digite o nome de uma cidade: ').strip()
separado = cidade.split()
print('SANTO' == separado[0].upper())


# RESOLUÇÃO GUANABARA
"""
cidade = input('Digite o nome de uma cidade: ').strip()
print(cidade[:5].upper() == 'SANTO')
"""