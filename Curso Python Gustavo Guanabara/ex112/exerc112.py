# DENTRO DO PACOTE UTILIDADESCEV QUE CRIAMOS NO DESAFIO 111, TEMOS UM MÓDULO CHAMADO DADO.
# CRIE UMA FUNÇÃO CHAMADA LEIADINHEIRO() QUE SEJA CAPAZ DE FUNCIONAR COMO A FUNÇÃO INPUT(), MAS COM UMA
# VALIDAÇÃO DE DADOS PARA ACEITAR APENAS VALORES QUE SEJA MONETÁRIOS

# MINHA RESOLUÇÃO
from UtilidadesCeV import moeda, dado

p_valido = dado.leiadinheiro()
moeda.resumo(p_valido, 10, 20)


# RESOLUÇÃO GUANABARA
"""from UtilidadesCeV import moeda, dado

p = dado.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(p, 10, 20)"""
