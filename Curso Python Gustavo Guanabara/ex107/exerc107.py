# CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS AUMENTAR(), DIMINUIR(), DOBRO() E METADE().
# FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES

# MINHA RESOLUÇÃO
import moeda

preco = float(input('Digite o preço: R$ '))
aumento = float(input('Digite a porcentagem de aumento: '))
reducao = float(input('Digite a porcentagem de redução: '))
print()
print(f'A metade de R$ {preco:.2f} é R$ {moeda.metade(preco):.2f}')
print(f'O dobro de R$ {preco:.2f} é R$ {moeda.dobro(preco):.2f}')
print(f'Aumentando {aumento}% de R$ {preco:.2f}, temos R$ {moeda.aumentar(preco, aumento):.2f}')
print(f'Reduzindo {reducao}% de R$ {preco:.2f}, temos R$ {moeda.diminuir(preco, reducao):.2f}')


# RESOLUÇÃO GUANABARA
"""import moeda

p = float(input('Digite o preço: R$ '))
print()
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Reduzindo 20%, temos R$ {moeda.diminuir(p, 20)}')"""
