# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

from datetime import datetime

ano = int(input('Digite um ano qualquer (0 para ano atual): '))
if ano == 0:
    ano = datetime.now().year
    print(f'O ano atual é {ano}')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
