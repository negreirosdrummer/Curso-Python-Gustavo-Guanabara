# DESAFIO 52
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO

# MINHA RESOLUÇÃO:
# primo = True
# num = int(input('Digite um número inteiro qualquer: '))
# if num <= 1:
#     primo = False
# for c in range(2, int(num ** 0.5) + 1):
#     if num % c == 0:
#         primo = False
# if primo:
#     print(f'{num} É um número PRIMO')
# elif not primo:
#     print(f'{num} NÃO É um número PRIMO')


# RESOLUÇÃO GUANABARA (consegui reproduzir vendo o funcionamento do programa)
num = int(input('Digite um número inteiro qualquer: '))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[31m{c}', end=' ')
        cont += 1
    else:
        print(f'\033[33m{c}', end=' ')
if cont == 2:
    print(f'\n\n\033[m{num} só foi divisível por 1 e por ele mesmo')
    print(f'E por isso ele É um número PRIMO!')
else:
    print(f'\n\n\033[mO número {num} foi divisível por {cont} números')
    print(f'Por isso ele NÃO É um número PRIMO!')
