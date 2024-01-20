# DESAFIO 83
# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES.
# SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA

# MINHA RESOLUÇÃO
lista = []
exp = input('Digite uma expressão: ')
for caractere in exp:
    if caractere == '(':
        lista.append('(')
    elif caractere == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expresão válida!')
else:
    print('Expressão inválida!')


# RESOLUÇÃO GUANABARA
expr = input('Digite uma expressão: ')
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expresão válida!')
else:
    print('Expressão inválida!')
