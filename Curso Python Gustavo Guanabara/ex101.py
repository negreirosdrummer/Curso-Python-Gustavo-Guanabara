# DESAFIO 101
# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE
# UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES

# MINHA RESOLUÇÃO

# from datetime import date


# sobre escopo de IMPORTAÇÃO: importar módulos dentro de funções economiza memória, pois o
# módulo só será usado na execução da função
# def voto(ano_nasc):
#     idade = ano_atual - ano_nasc
#     if idade < 16:
#         return f'Com {idade} anos: VOTO NEGADO'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# ano_atual = date.today().year
# print('-' * 30)
# ano_nasc = int(input('Em que ano você nasceu? '))
# print(voto(ano_nasc))


# RESOLUÇÃO GUANABARA
# sobre escopo de IMPORTAÇÃO: importar módulos dentro de funções economiza memória, pois o
# módulo só será usado na execução da função
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
