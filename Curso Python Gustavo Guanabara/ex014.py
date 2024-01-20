# DESAFIO 14
# ESCREVA UM PROGRAMA QUE LEIA UMA TEMPERATURA DIGITADA EM GRAUS CELSIUS E CONVERTA PARA GRAUS FAHRENHEIT

temp_c = float(input('Digite a temperatura em ºC: '))
temp_f = temp_c * 1.8 + 32
print(f'A temperatura de {temp_c}ºC corresponde a {temp_f}ºF')
