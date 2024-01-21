# DESAFIO 49
# REFAÇA O DESAFIO 9, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO "FOR"

num = int(input('Digite um número inteiro para ver sua tabuada: '))
print('-'*12)
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}')
print('-'*12)
