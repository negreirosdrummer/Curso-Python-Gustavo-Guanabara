#

# MINHA RESOLUÇÃO
def leiadinheiro():
    valido = False
    while not valido:
        p = str(input('Digite o preço: R$ ')).strip().replace(',', '.')
        if p.isalpha() or p == '':
            print(f'\033[31mERRO: "{p}" não é um valor válido!\033[m')
            valido = False
        else:
            p = float(p)
            valido = True
    return p


# RESOLUÇÃO GUANABARA
"""def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" não é um valor válido!\033[m')
        else:
            valido = True
            return float(entrada)"""
