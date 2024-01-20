# DESAFIO 25
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

nome = input('Digite o seu nome: ').strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
