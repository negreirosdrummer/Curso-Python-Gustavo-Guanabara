# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: INÍCIO, FIM E PASSO.
# SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
# DE 1 ATÉ 10, DE 1 EM 1
# DE 10 ATÉ 0, DE 2 EM 2
# UMA CONTAGEM PERSONALIZADA

# MINHA RESOLUÇÃO
'''from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo *= -1
    if inicio < fim and passo < 0:
        passo *= -1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:' if passo > 0
          else f'Contagem de {inicio} até {fim} de {-passo} em {-passo}:')
    tamanho = (fim - inicio) // passo + 1
    cont = 0
    soma = inicio
    while cont < tamanho:
        print(soma, end=' ')
        sleep(0.25)
        soma += passo
        cont += 1
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)'''


# RESOLUÇÃO GUANABARA
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.25)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.25)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
