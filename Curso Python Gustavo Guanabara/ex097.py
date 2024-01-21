# DESAFIO 97
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E
# MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL.
# EX: ESCREVA("OLÁ, MUNDO!")
# SAÍDA:
# ~~~~~~~~~~~
# OLÁ, MUNDO!
# ~~~~~~~~~~~

# MINHA RESOLUÇÃO
def escreva(txt):
    tamanho = len(txt)
    print('~' * tamanho)
    print(txt)
    print('~' * tamanho)


txt = input('Digite uma frase qualquer: ')
escreva(txt)


# RESOLUÇÃO GUANABARA
'''def escreva(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)


txt = input('Digite uma frase qualquer: ')
escreva(txt)'''
