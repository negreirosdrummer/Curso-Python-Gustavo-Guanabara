# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA.
# CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.
# NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE

# MINHA RESOLUÇÃO
lista = [1, 2, 6, 9, 20]
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    elif num in lista:
        print('Valores duplicados não podem ser adicionados')
    op = input('Continuar? [S/N] ').strip().upper()
    while op not in 'SN' or op == '':
        op = input('Opção inválida. Digite somente "S" ou "N": ').strip().upper()
    if op == 'N':
        break
print('-=' * 20)
if len(lista) == 1:
    print(f'Você digitou o valor {lista[0]}')
else:
    ordenada = sorted(lista)
    if len(lista) >= 2:
        print(f'Você digitou os valores ', end='')
        for n in range(len(ordenada)):
            if n < len(ordenada) - 2:
                print(ordenada[n], end=', ')
            elif n < len(ordenada) - 1:
                print(ordenada[n], end=' e ')
            else:
                print(ordenada[n])
