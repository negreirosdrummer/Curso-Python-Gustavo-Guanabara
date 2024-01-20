# DESAFIO 8
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS

metros = float(input('Digite um valor (m): '))
print(f'{metros} metros equivalem a {metros/1000:.4f} kilômetros')
print(f'{metros} metros equivalem a {metros/100:.3f} hectômetros')
print(f'{metros} metros equivalem a {metros/10:.2f} decâmetros')
print(f'{metros} metros equivalem a {metros*10:.0f} decímetros')
print(f'{metros} metros equivalem a {metros*100:.0f} centímetros')
print(f'{metros} metros equivalem a {metros*1000:.0f} milímetros')
