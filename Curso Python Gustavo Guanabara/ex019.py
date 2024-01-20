# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O
# NOME DOS ALUNOS E ESCREVENDO NA TELA O NOME DO ESCOLHIDO

import random
aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)

print(f'O aluno sorteado foi {sorteado}')
