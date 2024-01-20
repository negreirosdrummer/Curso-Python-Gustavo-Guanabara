# CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS AUMENTAR(), DIMINUIR(), DOBRO() E METADE().
# FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES

# MINHA RESOLUÇÃO
def aumentar(preco, aum):
    return preco + (preco * (aum / 100))


def diminuir(preco, redu):
    return preco - (preco * (redu / 100))


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2


# RESOLUÇÃO GUANABARA
"""def aumentar(p, taxa):
    res = p + (p * (taxa / 100))
    return res


def diminuir(p, taxa):
    res = p - (p * (taxa / 100))
    return res


def dobro(p):
    res = p * 2
    return res


def metade(p):
    res = p / 2
    return res"""
