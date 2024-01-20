# ADICIONE O MÓDULO MOEDA.PY CRIADO NOS DESAFIOS ANTERIORES, UMA FUNÇÃO CHAMADA RESUMO(), QUE
# MOSTRE NA TELA ALGUMAS INFORMAÇÕES GERADAS PELAS FUNÇÕES QUE JÁ TEMOS NO MÓDULO CRIADO ATÉ AQUI

# MINHA RESOLUÇÃO
"""import moeda

preco = float(input('Digite o preço: R$ '))
aumento = float(input('Digite a porcentagem de aumento: '))
reducao = float(input('Digite a porcentagem de redução: '))

moeda.resumo(preco, aumento, reducao)"""


# RESOLUÇÃO GUANABARA
import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 10)
