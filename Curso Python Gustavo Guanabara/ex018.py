# DESAFIO 18
# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO

import math

angulo = float(input('Digite um ângulo: '))
rad = angulo * 0.0174533
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'Seno de {angulo}: {sen:.2f}')
print(f'Cosseno de {angulo}: {cos:.2f}')
print(f'Tangente de {angulo}: {tan:.2f}')
