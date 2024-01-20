# ADAPTE O CÓDIGO DO DESAFIO #107, CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA MOEDA() QUE CONSIGA
# MOSTRAR OS NÚMEROS COMO UM VALOR MONETÁRIO FORMATADO

# MINHA RESOLUÇÃO
def moeda(preco):
    return f'R$ {preco:.2f}'.replace(".", ",")


def aumentar(preco, aum):
    return f'R$ {preco + (preco * (aum / 100)):.2f}'.replace(".", ",")


def diminuir(preco, redu):
    return f'R$ {preco - (preco * (redu / 100)):.2f}'.replace(".", ",")


def dobro(preco):
    return f'R$ {preco * 2:.2f}'.replace(".", ",")


def metade(preco):
    return f'R$ {preco / 2:.2f}'.replace(".", ",")


# RESOLUÇÃO GUANABARA

"""def aumentar(preco=0, taxa=0):
    res = preco + (preco * (taxa / 100))
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * (taxa / 100))
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')"""
