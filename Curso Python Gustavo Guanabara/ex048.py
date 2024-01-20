# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS QUE SÃO
# MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1

# print com variável contadora (não foi pedido no enunciado, mas estava na resolução final)
print(f'A soma de todos os {cont} valores solicitados é {soma}')

# print sem a variável contadora (minha resolução original)
print(f'A soma de todos os números ímpares que são múltiplos de 3 no intervalo de 1 a 500 é {soma}')
