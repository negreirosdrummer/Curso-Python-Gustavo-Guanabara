# DESAFIO 75
# DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
# QUANTAS VEZES APARECEU O VALOR 9
# EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
# QUAIS FORAM OS NÚMEROS PARES

# MINHA RESOLUÇÃO
lista = []
for c in range(4):
    num = int(input('Digite um número: '))
    lista.append(num)
tupla = tuple(lista)
print('Você digitou os valores', tupla)

if 9 in tupla:
    if tupla.count(9) == 1:
        print(f'O número 9 apareceu {tupla.count(9)} vez.')
    else:
        print(f'O número 9 apareceu {tupla.count(9)} vezes.')
else:
    print('O número 9 não aparece nessa tupla')
if 3 in tupla:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado')
print('Os números pares foram: ', end='')
for n in range(len(tupla)):
    if tupla[n] % 2 == 0:
        print(tupla[n], end=' ')


# RESOLUÇÃO GUANABARA
'''num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 aparece pela primeira vez na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado')
print('Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')'''
