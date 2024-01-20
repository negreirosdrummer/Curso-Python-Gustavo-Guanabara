# DESAFIO 44
# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM
# PRODUTO, CONSIDERANDOO SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# – À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
# – À VISTA NO CARTÃO: 5% DE DESCONTO
# – EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# – 3X OU MAIS NO CARTÃO: 20% DE JUROS

print(f'{" LOJAS NEGREIROS ":=^40}')
preco_prod = float(input('Informe o valor do produto: R$ '))
print("""\nFORMAS DE PAGAMENTO:
1 - À vista (dinheiro/cheque): 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - 2x no cartão: preço normal 
4 - 3x ou mais no cartão: 20% de juros
""")
opcao = int(input('Digite o número da opção desejada: '))

if opcao == 1:
    print('A opção escolhida foi "à vista"')
    print(f'O valor final da compra (com 10% de desconto) é de R$ {preco_prod * 0.9:.2f}')
elif opcao == 2:
    print('A opção escolhida foi "à vista no cartão"')
    print(f'O valor final da compra (com 5% de desconto) é de R$ {preco_prod * 0.95:.2f}')
elif opcao == 3:
    print('A opção escolhida foi "2x no cartão"')
    print(f'Sua compra será parcelada em 2x de R$ {preco_prod / 2:.2f} SEM JUROS')
    print(f'O valor final da compra é de R$ {preco_prod:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R$ {preco_prod * 1.2 / parcelas:.2f} COM JUROS')
    print(f'O valor final da compra (com acréscimo de 20% de juros) é de R$ {preco_prod * 1.2:.2f}')
else:
    print('\033[31mOPÇÃO INVÁLIDA')
