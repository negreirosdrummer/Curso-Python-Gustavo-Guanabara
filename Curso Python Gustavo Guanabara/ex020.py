# DESAFIO 20
# O MESMO PROFESOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS.
# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA

import random
aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print(f'A ordem de apresentação é:\n{lista}')
