# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS.
# O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR OU NÃO.
# NO FINAL, MOSTRE:
# QUAL É O TOTAL GASTO NA COMPRA
# QUANTOS PRODUTOS CUSTAM MAIS DE R$1000
# QUAL É O NOME DO PRODUTO MAIS BARATO

# MINHA RESOLUÇÃO
print('--' * 15)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('--' * 15)
total = 0
total_1000 = 0
mais_barato = ' '
menor_preço = 0
cont = 0
while True:
    nome = input('Nome do produto: ').strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preço < menor_preço:
        menor_preço = preço
        mais_barato = nome
    if preço > 1000:
        total_1000 += 1
    total += preço
    cont += 1
    continuar = input('Adicionar mais produtos? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção Inválida. Adicionar mais produtos? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('{:-^40}'.format(" FIM DO PROGRAMA "))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {total_1000} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi {mais_barato} que custa R$ {menor_preço:.2f}')
