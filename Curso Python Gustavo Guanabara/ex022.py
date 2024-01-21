# DESAFIO 22
# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# – O NOME COM TODAS AS LETRAS MAIÚSCULAS E MINÚSCULAS
# – QUANTAS LETRAS NO TOTAL (SEM CONSIDERAR ESPAÇOS)
# – QUANTAS LETRAS TEM O PRIMEIRO NOME

# MINHA RESOLUÇÃO
"""nome = input('Digite o seu nome completo: ').strip()
print(f'O seu nome com letras maiúsculas é: {nome.upper()}')
print(f'O seu nome com letras minúsculas é: {nome.lower()}')
separado = nome.split()
sem_espacos = ''.join(nome.split())
print(f'Seu nome tem {len(sem_espacos)} letras')
print(f'Seu primeiro nome é {separado[0]} e ele tem {len(separado[0])} letras')
"""

# RESOLUÇÃO GUANABARA
nome = input('Digite o seu nome completo: ').strip()
print(f'O seu nome com letras maiúsculas é: {nome.upper()}')
print(f'O seu nome com letras minúsculas é: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
