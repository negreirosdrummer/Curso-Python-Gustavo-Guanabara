# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50

# O PROBLEMA DA SOLUÇÃO SEGUINTE É QUE O PROGRAMA FAZ VÁRIAS ITERAÇÕES INÚTEIS TESTANDO A CONDIÇÃO
# for c in range(1, 51):
#     if c % 2 == 0:
#         print(c, end=' ')
# print('ACABOU!')

# A RESOLUÇÃO A SEGUIR FAZ SOMENTE AS ITERAÇÕES NECESSÁRIAS
for c in range(2, 51, 2):
    print(c, end=' ')
print('ACABOU!')