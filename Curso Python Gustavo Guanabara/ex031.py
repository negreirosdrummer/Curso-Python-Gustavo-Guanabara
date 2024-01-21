# DESAFIO 31
# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS DE ATÉ 200 KM E R$ 0,45 PARTA VIAGENS MAIS LONGAS.

dist = float(input('Digite a distância da viagem (km): '))
if 0 < dist <= 200:
    print(f'O valor da passagem é de R${dist * 0.5:.2f}')
else:
    print(f'O valor da passagem é de R${dist * 0.45:.2f}')

# usando condição simplificada:
preco = 0.5 * dist if 0 < dist <= 200 else 0.45 * dist
print(f'O valor da passagem é de R${preco:.2f}')
