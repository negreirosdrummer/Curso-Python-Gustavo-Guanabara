# REESCREVA A FUNÇÃO LEIAINT() QUE FIZEMOS NO DESAFIO 104, INCLUINDO AGORA A POSSIBILIDADE DA DIGITAÇÃO DE
# UM NÚMERO DE TIPO INVÁLIDO. APROVEITE E CRIE TAMBÉM UMA FUNÇÃO LEIAFLOAT() COM A MESMA FUNCIONALIDADE

# MINHA RESOLUÇÃO
"""def leiaint():
    ok = False
    valor = 0
    while True:
        try:
            n = str(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            print('\033[0;31m\nO usuário preferiu não digitar esse número.\033[m')
            break
        try:
            valor = int(n)
            ok = True
        except ValueError:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
        if ok:
            break
    return valor


def leiafloat():
    ok = False
    valor = 0
    while True:
        try:
            n = str(input('Digite um número real: '))
        except KeyboardInterrupt:
            print('\033[0;31m\nO usuário preferiu não digitar esse número.\033[m')
            break
        try:
            valor = float(n)
            ok = True
        except ValueError:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        if ok:
            break
    return valor


inteiro = leiaint()
real = leiafloat()
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')"""


# RESOLUÇÃO GUANABARA
def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


inteiro = leiaint()
real = leiafloat()
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
