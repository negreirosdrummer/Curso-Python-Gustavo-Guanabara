# DESAFIO 56
# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS.
# NO FINAL DO PROGRAMA, MOSTRE:
# A MÉDIA DE IDADE DO GRUPO, QUAL É O NOME DO HOMEM MAIS VELHO E QUANTAS MULHERES TÊM MENOS DE 20 ANOS

soma_idades = 0
idade_hmaisvelho = 0
qtd_mulheres20 = 0
nome_hmaisvelho = ''
for c in range(0, 4):
    sexo = ' '
    print(f'----- {c+1}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    soma_idades += idade
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()
    # poderia usar 'if sexo in "Mm"' se não usasse o método .upper() na linha acima
    if sexo == 'M' and idade > idade_hmaisvelho:
        nome_hmaisvelho = nome
        idade_hmaisvelho = idade
    # poderia usar 'if sexo in "Ff"' se não usasse o método .upper() no input da variável 'sexo'
    if sexo == 'F' and idade < 20:
        qtd_mulheres20 += 1

media_idade = soma_idades / 4
print(f'A média de idade do grupo é de {media_idade} anos')
if idade_hmaisvelho == 0:
    print('Não existem homens nesse grupo')
else:
    print(f'O homem mais velho tem {idade_hmaisvelho} anos e se chama {nome_hmaisvelho}')
if qtd_mulheres20 == 1:
    print(f'{qtd_mulheres20} mulher tem menos de 20 anos')
elif qtd_mulheres20 > 1:
    print(f'{qtd_mulheres20} mulheres têm menos de 20 anos')
