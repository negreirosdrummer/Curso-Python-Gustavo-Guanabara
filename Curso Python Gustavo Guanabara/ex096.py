# DESAFIO 96
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM
# TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO

# MINHA RESOLUÇÃO
def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno de {larg:.2f} x {comp:.2f} é de {area:.2f}m²')


print('-' * 40)
print(f'{"CONTROLE DE TERRENOS":^40}')
print('-' * 40)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)



# RESOLUÇÃO GUANABARA FOI IGUAL
