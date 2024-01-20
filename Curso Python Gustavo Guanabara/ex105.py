# DESAFIO 105
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E
# VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
# – QUANTIDADE DE NOTAS
# – A MAIOR NOTA
# – A MENOR NOTA
# – A MÉDIA DA TURMA
# – A SITUAÇÃO (OPCIONAL)

# MINHA RESOLUÇÃO

# def notas(*notas, sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param notas: uma ou mais notas dos alunos
#     :param sit: (opcional) indica se deve ou não mostrar a situação da turma
#     :return: dicionário com várias informações sobre as notas
#     """
#     print(notas)
#     dict = {}
#     dict['total'] = len(notas)
#     soma = 0
#     for c in range(len(notas)):
#         soma += notas[c]
#         if c == 0:
#             maior = menor = notas[0]
#         else:
#             if notas[c] > maior:
#                 maior = notas[c]
#             elif notas[c] < menor:
#                 menor = notas[c]
#     dict['maior'] = maior
#     dict['menor'] = menor
#     dict['media'] = soma / len(notas)
#     if sit:
#         if dict['media'] >= 7:
#             dict['situação'] = 'BOA!'
#         elif 5 <= dict['media'] < 7:
#             dict['situação'] = 'RAZOÁVEL'
#         else:
#             dict['situação'] = 'RUIM'
#     return dict


# resp = notas(8, 7, 5, sit=True)
# print(resp)
# help(notas)


# RESOLUÇÃO GUANABARA

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA!'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(8, 7, 10, sit=True)
print(resp)
help(notas)
