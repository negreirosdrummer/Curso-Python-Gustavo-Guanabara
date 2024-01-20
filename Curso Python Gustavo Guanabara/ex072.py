# DESAFIO 72
# CRIE UM PROGRAMA QUE TENHA UMA DUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.
# SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (DE 0 A 20) E MOSTRÁ-LO POR EXTENSO

# MINHA RESOLUÇÃO
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número inteiro de 0 a 20: '))
    while not 0 <= num <= 20:
        num = int(input('Número inválido. Digite um valor de 0 a 20: '))
    else:
        print(f'{num} escrito por extenso é "{extenso[num]}"')
    continuar = input('Continuar? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Digite S ou N: ').strip().upper()
    if continuar == 'N':
        break
