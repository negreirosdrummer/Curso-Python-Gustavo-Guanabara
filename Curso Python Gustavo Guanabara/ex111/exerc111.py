# CRIE UM PACOTE CHAMADO UTILIDADESCEV QUE TENHA DOIS MÓDULOS INTERNOS CHAMADOS "MOEDA" E "DADO".
# TRANSFIRA TODAS AS FUNÇÕES UTILIZADAS NOS DESAFIOS 107, 108 E 109 PARA O PRIMEIRO PACOTE E MANTENHA TUDO FUNCIONANDO

# MINHA RESOLUÇÃO
"""import moeda

preco = float(input('Digite o preço: R$ '))
aumento = float(input('Digite a porcentagem de aumento: '))
reducao = float(input('Digite a porcentagem de redução: '))

moeda.resumo(preco, aumento, reducao)"""


# RESOLUÇÃO GUANABARA
from UtilidadesCeV import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 10)
