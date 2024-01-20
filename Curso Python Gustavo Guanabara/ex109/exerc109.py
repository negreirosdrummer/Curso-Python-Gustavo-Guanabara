# MODIFIQUE AS FUNÇÕES QUE FORM CRIADAS NO DESAFIO 107 PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE
# O VALOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO PELA FUNÇÃO MOEDA(), DESENVOLVIDA NO DESAFIO 108

# MINHA RESOLUÇÃO
"""import moeda

preco = float(input('Digite o preço: R$ '))
aumento = float(input('Digite a porcentagem de aumento: '))
reducao = float(input('Digite a porcentagem de redução: '))
f = input('Deseja exibir a unidade monetária formatada? [S/N] ').strip().upper()
while f not in 'SN':
    f = input('Deseja exibir a unidade monetária formatada? [S/N] ').strip().upper()
if f == 'S':
    formatar = True
elif f == 'N':
    formatar = False
print()
print(f'A metade de {moeda.moeda(preco, formatar)} é {moeda.metade(preco, formatar)}')
print(f'O dobro de {moeda.moeda(preco, formatar)} é {moeda.dobro(preco, formatar)}')
print(f'Aumentando {aumento}% de {moeda.moeda(preco, formatar)}, temos {moeda.aumentar(preco, aumento, formatar)}')
print(f'Reduzindo {reducao}% de {moeda.moeda(preco, formatar)}, temos {moeda.diminuir(preco, reducao, formatar)}')"""


# RESOLUÇÃO GUANABARA
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {moeda.moeda(p)}, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 50% de {moeda.moeda(p)}, temos {moeda.diminuir(p, 50, True)}')
