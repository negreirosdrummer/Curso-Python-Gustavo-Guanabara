# CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-O (COM IDADE) EM UM DICIONÁRIO.
# SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO.
# CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR

# MINHA RESOLUÇÃO
from datetime import date

pessoa = dict()
pessoa['nome'] = input('Nome: ')
pessoa['ano_nasc'] = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - pessoa['ano_nasc']
pessoa['ctps'] = int(input('CTPS (0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] + 35) - pessoa['ano_nasc']
print('-=' * 20)
print('DADOS PESSOAIS:')
# for k, v in pessoa.items():
#     print(f'{k}: {v}')

print(f'\tNome: {pessoa["nome"]}')
print(f'\tIdade: {pessoa["idade"]}')
print(f'\tCTPS: {pessoa["ctps"]}')
if pessoa['ctps'] != 0:
    print(f'\tAno de Contratação: {pessoa["contratacao"]}')
    print(f'\tSalário: R$ {pessoa["salario"]:.2f}')
    print(f'\tIdade de Aposentadoria: {pessoa["aposentadoria"]} anos')


# RESOLUÇÃO GUANABARA
'''from datetime import date

dados = dict()
dados['Nome'] = input('Nome: ')
dados['Nascimento'] = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - dados['Nascimento']
dados['CTPS'] = int(input('CTPS (0 se não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - dados['Nascimento']
print('-=' * 20)
for k, v in dados.items():
    print(f'{k}: {v}')'''
