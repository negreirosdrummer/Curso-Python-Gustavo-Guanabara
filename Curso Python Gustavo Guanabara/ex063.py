# DESAFIO 63
# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA
# TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI. EXEMPLO:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

# MINHA RESOLUÇÃO (funciona com qualquer valor digitado - a do Guanabara não funciona se o valor digitado for 1)
print('-=' * 11)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 11)
num = int(input('Quantos termos deseja mostrar? '))

a = 0
b = 1
cont = 0
while cont < num:
    if cont == 0:
        print(a, end='\033[32m -> \033[m')
        cont += 1
    elif cont == 1:
        print(b, end='\033[32m -> \033[m')
        cont += 1
    else:
        fibonacci = a + b
        a = b
        b = fibonacci
        cont += 1
        if cont != num:
            print(fibonacci, end='\033[32m -> \033[m')
        elif cont == num:
            print(fibonacci)
print('FIM')


# RESOLUÇÃO GUANABARA - não funciona se quiser mostrar somente 1 termo (sempre mostra 0 e 1 por padrão)
# print('-=' * 11)
# print('SEQUÊNCIA DE FIBONACCI')
# print('-=' * 11)
# num = int(input('Quantos termos deseja mostrar? '))
# t1 = 0
# t2 = 1
# print(f'{t1} -> {t2}', end='')
# cont = 3  # inicia no 3, pois os 2 primeiros termos são sempre 0 e 1
# while cont <= num:
#     t3 = t1 + t2
#     print(f' -> {t3}', end='')
#     t1 = t2
#     t2 = t3
#     cont += 1
# print(' -> FIM')
