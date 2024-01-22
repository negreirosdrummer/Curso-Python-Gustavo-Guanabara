# DESAFIO 89
# CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA.
# NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E
# PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE

# MINHA RESOLUÇÃO
"""
alunos = []
aluno = []
notas = []
while True:
    aluno.clear()
    notas.clear()
    nome = input('Nome: ')
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    notas.append(nota1)
    nota2 = float(input('Nota 2: '))
    notas.append(nota2)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    continuar = input('Adicionar mais alunos? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Digite somente S ou N: ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 16)
print(f'{"Nº":<6}', end='')
print(f'{"NOME":<15}', end='')
print(f'{"MÉDIA"}')

print('-' * 27)
for i in range(len(alunos)):
    soma = 0
    print(f'{i + 1:<6}', end='')
    print(f'{alunos[i][0]:<15}', end='')

    for j in range(len(alunos[i][1])):
        soma += alunos[i][1][j]
    media = soma/2
    print(f'{media:.1f}')
print('-' * 27)

while True:
    num_aluno = int(input('Mostrar notas de qual aluno? (999 para sair) '))
    if num_aluno == 999:
        break
    elif 0 < num_aluno <= len(alunos):
        print(f'As notas de {alunos[num_aluno - 1][0]} são {alunos[num_aluno - 1][1]}')
        print('-' * 48)
    else:
        print('Digite um número válido!')
        print('-' * 48)

print('\nFinalizando...')
print('<<< Volte sempre! >>>')
"""


# RESOLUÇÃO GUANABARA
ficha = []
while True:
    nome = (str(input("Nome: ")))
    nota1 = (float(input("Nota 1: ")))
    nota2 = (float(input("Nota 2: ")))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in "Nn":
        break

print("-=" * 30)
print(f"{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 30)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
print("-" * 30)
while True:
    print("-" * 30)
    opcao = int(input("Mostrar notas de qual aluno? (999 para sair): "))
    if opcao == 999:
        print("FINALIZANDO...")
        break
    if opcao <= len(ficha) - 1:
        print(f"Notas de {ficha[opcao][0]} são {ficha[opcao][1]}")
print("<<< VOLTE SEMPRE >>>")
