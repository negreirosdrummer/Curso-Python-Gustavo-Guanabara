# ADAPTE O CÓDIGO DO DESAFIO #107, CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA MOEDA() QUE CONSIGA
# MOSTRAR OS NÚMEROS COMO UM VALOR MONETÁRIO FORMATADO

# MINHA RESOLUÇÃO
import moeda

preco = float(input('Digite o preço: R$ '))
aumento = float(input('Digite a porcentagem de aumento: '))
reducao = float(input('Digite a porcentagem de redução: '))
print()
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}')
print(f'O dobro de R$ {moeda.moeda(preco)} é {moeda.dobro(preco)}')
print(f'Aumentando {aumento:.0f}% de {moeda.moeda(preco)}, temos {moeda.aumentar(preco, aumento)}')
print(f'Reduzindo {reducao:.0f}% de {moeda.moeda(preco)}, temos {moeda.diminuir(preco, reducao)}')


# RESOLUÇÃO GUANABARA
"""import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 50% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.diminuir(p, 50))}')"""
