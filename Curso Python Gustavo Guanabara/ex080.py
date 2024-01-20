# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM
# UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT()). NO FINAL, MOSTRE A LISTA ORDENADA NA TELA

# MINHA RESOLUÇÃO (NÃO CONSEGUI TERMINAR)
'''lista = []
maior = 0
menor = 0
for n in range(5):
    num = int(input('Digite um valor: '))
    if n == 0:
        lista.append(num)
        print('Adicionado à lista')
        maior = menor = num
    elif n > 0:
        if num >= maior:
            lista.insert(lista.index(maior) + 1, num)
            print('Adicionado ao final da lista')
            maior = num
        elif num <= menor:
            lista.insert(lista.index(menor), num)
            print(f'Adicionado à posição {lista.index(menor)} da lista')
            menor = num
print(lista)'''


# 2ª TENTATIVA (DEPOIS DE VER A CORREÇÃO DO EXERCÍCIO)
lista = []
for n in range(5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        for n in lista:
            if num <= n:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)

# RESOLUÇÃO GUANABARA
lista = []

for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
print("-="*30)
print(f"Os valores digitados em ordem foram {lista}")
