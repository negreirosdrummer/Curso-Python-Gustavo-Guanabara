# DESAFIO 104
# CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE À FUNÇÃO INPUT() DO PYTHON,
# SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO. EX: N = LEIAINT(‘DIGITE UM N: ‘)

# MINHA RESOLUÇÃO (NÃO CONSEGUI FINALIZAR)

# def leiaint(n):
#     if n is int:
#         return f'Você acabou de digitar o número {n}'
#     else:
#         return '\033[31mERRO! Digite um número inteiro válido!'


# n = leiaint('Digite um número: ')


# RESOLUÇÃO GUANABARA

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
