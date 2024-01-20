# MODIFIQUE AS FUNÇÕES QUE FORM CRIADAS NO DESAFIO 107 PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE
# O VALOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO PELA FUNÇÃO MOEDA(), DESENVOLVIDA NO DESAFIO 108

# MINHA RESOLUÇÃO
"""def moeda(p, formatar):
    if formatar:
        return f'R$ {p:.2f}'
    else:
        return p


def aumentar(p, aum, formatar):
    if formatar:
        return f'R$ {p + (p * (aum / 100)):.2f}'
    else:
        return p + (p * (aum / 100))


def diminuir(p, redu, formatar):
    if formatar:
        return f'R$ {p - (p * (redu / 100)):.2f}'
    else:
        return p - (p * (redu / 100))


def dobro(p, formatar):
    if formatar:
        return f'R$ {p * 2:.2f}'
    else:
        return p * 2


def metade(p, formatar):
    if formatar:
        return f'R$ {p / 2:.2f}'
    else:
        return p / 2"""


# RESOLUÇÃO GUANABARA

def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * (taxa / 100))
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * (taxa / 100))
    return res if not formato else moeda(res)


def dobro(preco, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')
