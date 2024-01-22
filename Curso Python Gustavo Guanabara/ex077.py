# DESAFIO 77
# CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS).
# DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
         'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in tupla:
    print(f'Na palavra {palavra.upper()} temos as vogais ', end='')
    for letra in palavra:
        if letra in 'aeiou':  # se quisesse verificar os acentos, era só incluir na lista (áâãéê), etc
            print(letra, end=' ')
    print()
