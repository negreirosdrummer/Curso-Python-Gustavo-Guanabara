# DESAFIO 17
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E
# MOSTRE O COMPRIMENTO DA HIPOTENUSA

# MINHA REOSLUÇÃO
"""
cat_oposto = float(input('Digite a medida do cateto oposto: '))
cat_adjacente = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = (cat_oposto ** 2 + cat_adjacente ** 2) ** (1/2)
print(f'A hipotenusa do triângulo retângulo com catetos de {cat_oposto}cm e {cat_adjacente}cm é de {hipotenusa:.2f}cm')
"""


# RESOLUÇÃO GUANABARA
from math import hypot
cat_oposto = float(input('Digite a medida do cateto oposto: '))
cat_adjacente = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)
print(f'A hipotenusa do triângulo retângulo com catetos de {cat_oposto}cm e {cat_adjacente}cm é de {hipotenusa:.2f}cm')
