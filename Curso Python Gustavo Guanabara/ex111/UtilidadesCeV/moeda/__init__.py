# ADICIONE O MÓDULO MOEDA.PY CRIADO NOS DESAFIOS ANTERIORES, UMA FUNÇÃO CHAMADA RESUMO(), QUE
# MOSTRE NA TELA ALGUMAS INFORMAÇÕES GERADAS PELAS FUNÇÕES QUE JÁ TEMOS NO MÓDULO CRIADO ATÉ AQUI

# MINHA RESOLUÇÃO
"""def resumo(p, aum, redu):
    print('--' * 20)
    print(f"{'RESUMO DO VALOR':^40}")
    print('--' * 20)
    print(f'{"Preço analisado:":<20} {moeda(p)}')
    print(f'{"Metade do preço:":<20} {metade(p)}')
    print(f'{"Dobro do preço:":<20} {dobro(p)}')
    print(f'{f"{aum:.0f}% de aumento:":<20} {aumentar(p, aum)}')
    print(f'{f"{redu:.0f}% de redução:":<20} {diminuir(p, redu)}')


def moeda(p):
    return f'R$ {p:.2f}'


def aumentar(p, aum):
    return f'R$ {p + (p * (aum / 100)):.2f}'


def diminuir(p, redu):
    return f'R$ {p - (p * (redu / 100)):.2f}'


def dobro(p):
    return f'R$ {p * 2:.2f}'


def metade(p):
    return f'R$ {p / 2:.2f}'"""


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


def resumo(preco, taxaa, taxar):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":<20} {moeda(preco)}')
    print(f'{"Metade do preço:":<20} {metade(preco, True)}')
    print(f'{"Dobro do preço:":<20} {dobro(preco, True)}')
    print(f'{f"{taxaa}% de aumento:":<20} {aumentar(preco, taxaa, True)}')
    print(f'{f"{taxar}% de redução:":<20} {diminuir(preco, taxar, True)}')
    print('-' * 30)
