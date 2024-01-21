# DESAFIO 34
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$1250,00, CALCULE UM AUMENTO DE 10%. PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

salario = float(input('Digite o salário atual: R$ '))
if salario > 1250:
    salario_aumento = salario * 1.1
    print(f'O salário com aumento de 10% equivale a R$ {salario_aumento:.2f}')
if salario <= 1250:
    salario_aumento = salario * 1.15
    print(f'O salário com aumento de 15% equivale a R$ {salario_aumento:.2f}')
