# DESAFIO 81
# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
# DEPOIS DISSO, MOSTRE:
# QUANTOS NÚMEROS FORAM DIGITADOS
# A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE
# SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA

# MINHA RESOLUÇÃO
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = input('Continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Digite somente S ou N: ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Foram digitados {len(lista)} números')
print(f'A lista ordenada de forma decrescente é: {sorted(lista, reverse=True)}')
if lista.count(5) == 1:
    print(f'O valor 5 está na lista na {lista.index(5) + 1}ª posição')
elif lista.count(5) > 1:
    print('O valor 5 está na lista nas posições ', end='')
    cont = lista.count(5)
    for i, j in enumerate(lista):
        if lista[i] == 5 and cont > 2:
            print(f'{i + 1}', end=', ')
            cont -= 1
        elif lista[i] == 5 and cont == 2:
            print(f'{i + 1}', end=' e ')
            cont -= 1
        elif lista[i] == 5 and cont == 1:
            print(f'{i + 1}')
else:
    print('O valor 5 não está na lista')


# MINHA RESOLUÇÃO SIMPLIFICADA
"""
lista = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    opcao = " "
    while opcao not in "NnSs":
        opcao = input("Deseja continuar? [S/N]: ").strip().upper()
    if opcao in "Nn":
        break

print(f"Você digitou {len(lista)} elementos")
print(f"Os valores em ordem decrescente são {sorted(lista, reverse=True)}")
if 5 in lista:
    pos5 = []
    for pos in range(len(lista)):
        if lista[pos] == 5:
            pos5.append(pos)
if lista.count(5) == 1:
    print(f"O valor 5 faz parte da lista na posição {pos5}!")  # pode mostrar em que posições o 5 se encontra
elif lista.count(5) > 1:
    print(f"O valor 5 faz parte da lista nas posições {pos5}!")
elif 5 not in lista:
    print("O valor 5 não foi encontrado na lista!")
"""


# RESOLUÇÃO GUANABARA
"""
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem crescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista')
"""
