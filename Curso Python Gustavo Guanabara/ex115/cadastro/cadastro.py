def ver_cadastros():
    print('-' * 50)
    print(f'{"PESSOAS CADASTRADAS":^50}')
    print('-' * 50)
    cadastro = open('cadastro.txt', 'r')
    pessoas = cadastro.read()
    print(pessoas)


def fazer_cadastro():
    print('-' * 50)
    print(f'{"NOVO CADASTRO":^50}')
    print('-' * 50)
    cadastro = open('cadastro.txt', 'a')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cadastro.write(f'\n{nome:<30}')
    cadastro.write(f'{str(idade)} anos')
    print(f'Cadastro de {nome} realizado com sucesso!')
