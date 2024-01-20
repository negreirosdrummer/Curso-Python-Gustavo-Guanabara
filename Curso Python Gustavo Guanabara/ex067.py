# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO.
# O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO

# MINHA RESOLUÇÃO
while True:
    cont = 1
    num = int(input('Quer ver a tabuada de qual valor? (Digite um valor negativo para sair) '))
    print('-=' * 35)
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    print('-=' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
