# CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS PELOS SEUS NOMES E
# IDADES EM UM ARQUIVO DE TEXTO SIMPLES. O SISTEMA SÓ VAI TER DUAS OPÇÕES:
# CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS

# MINHA RESOLUÇÃO
from cadastro import cadastro

while True:
    print('-' * 50)
    print(f'{"MENU PRINCIPAL":^50}')
    print('-' * 50)
    print('\033[32m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[32m2\033[m - \033[34mCadastrar nova pessoa\033[m')
    print('\033[32m3\033[m - \033[34mSair do sistema\033[m')
    print('-' * 50)
    try:
        op = int(input('Sua opção: '))
        if op == 1:
            cadastro.ver_cadastros()
        elif op == 2:
            cadastro.fazer_cadastro()
        elif op == 3:
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
    except ValueError:
        print('\033[31mDigite apenas o número da opção.\033[m')
print('-' * 50)
print(f'{"Saindo do sistema... Até logo!":^50}')
print('-' * 50)


# RESOLUÇÃO GUANABARA
