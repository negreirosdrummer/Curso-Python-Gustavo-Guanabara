# DESAFIO 37
# ESCREVA UM PROGRAMA EM PYTHON QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A
# BASE DE CONVERSÃO: OPÇÃO 1 PARA BINÁRIO, 2 PARA OCTAL E 3 PARA HEXADECIMAL

num = int(input('Digite um número inteiro qualquer: '))
print('-=' * 13)
print('MENU DE OPÇÕES')
print("""1 - Converter para BINÁRIO
2 - Converter para OCTAL
3 - Converter para HEXADECIMAL
""")
print('-=' * 13)
opcao = int(input('Escolha a opção desejada: '))

if opcao == 1:
    print(f'O número {num} convertido para binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Opção Inválida!')
