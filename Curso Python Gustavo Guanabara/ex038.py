# DESAFIO 38
# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA DAS MENSAGENS:
# – O PRIMEIRO VALOR É MAIOR
# – O SEGUNDO VALOR É MAIOR
# – NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

num1 = int(input('Digite um número inteiro qualquer: '))
num2 = int(input('Digite outro número inteiro qualquer: '))

if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O segundo valor é maior!')
else:
    print('Os números são iguais!')
