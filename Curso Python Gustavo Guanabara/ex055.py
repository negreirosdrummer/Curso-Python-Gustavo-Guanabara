# DESAFIO 55
# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS.
# NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS

maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa (Kg): '))
    if c == 1:
        menor_peso = maior_peso = peso
    else:
        if peso >= maior_peso:
            maior_peso = peso
        elif peso <= menor_peso:
            menor_peso = peso

print(f'O maior peso foi de {maior_peso}Kg')
print(f'O menor peso foi de {menor_peso}Kg')
