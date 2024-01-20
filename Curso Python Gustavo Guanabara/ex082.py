# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
# DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS
# VALORES PARES E OS VALORES ÍMPARES DIGITADOS, RESPECTIVAMENTE.
# AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS

# MINHA RESOLUÇÃO
lista = []
lista_pares = []
lista_impares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = input('Continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Digite somente S ou N: ').strip().upper()
    if continuar == 'N':
        break

for num in lista:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {lista_pares}')
print(f'A lista de números ímpares é {lista_impares}')


# RESOLUÇÃO GUANABARA
'''num = []
pares = []
impares = []

while True:
    num.append(int(input("Digite um valor: ")))
    opcao = " "
    while opcao not in "NnSs":
        opcao = input("Deseja continuar? [S/N]: ").strip().upper()
    if opcao in "Nn":
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f"A lista completa é {num}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")'''
