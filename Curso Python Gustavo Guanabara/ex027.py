# DESAFIO 27
# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE

nome = input('Digite o seu nome completo: ').strip()
separado = nome.split()

print(f'O primeiro nome é {separado[0]}')
print(f'O último nome é {separado[len(separado) - 1]}')
