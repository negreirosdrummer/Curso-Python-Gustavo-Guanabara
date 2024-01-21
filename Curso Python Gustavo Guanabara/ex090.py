# DESAFIO 90
# FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO.
# NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA

# MINHA RESOLUÇÃO
aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = '\033[32mAPROVADO!'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = '\033[33mRECUPERAÇÃO'
elif aluno['media'] < 5:
    aluno['situação'] = '\033[31mREPROVADO'

print('-=' * 15)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["situação"]}')


# RESOLUÇÃO GUANABARA
'''aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO!'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'

print('-=' * 15)
for k, v in aluno.items():
    print(f'{k}: {v}')'''
