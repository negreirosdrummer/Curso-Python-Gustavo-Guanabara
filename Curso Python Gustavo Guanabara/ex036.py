# DESAFIO 36
# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
# PERGUNTE O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
# A PRESTAÇÃO MENSAL NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO

valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Em quantos anos deseja financiar? '))

limite = salario * 0.3
prestacao_mensal = valor_casa / (anos * 12)

print(f'\nPara pagar uma casa de R$ {valor_casa:.2f} em {anos} anos, a prestação será de R$ {prestacao_mensal:.2f}')
if prestacao_mensal > limite:
	print(f'Esse valor excede o limite de 30% do salário (R${limite:.2f})')
	print('\033[1;31mEMPRÉSTIMO NEGADO.')
else:
	print(f'Esse valor está dentro do limite de 30% do salário (R${limite:.2f})')
	print('\033[1;32mEMPRÉSTIMO APROVADO!')
