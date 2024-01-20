# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE
# NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
# – ATÉ 9 ANOS: MIRIM
# – ATÉ 14 ANOS: INFANTIL
# – ATÉ 19 ANOS: JÚNIOR
# – ATÉ 25 ANOS: SÊNIOR
# – ACIMA DE 25 ANOS: MASTER

from datetime import datetime

ano_nasc = int(input('Informe o ano de nascimento: '))
idade = datetime.now().year - ano_nasc
print(f'A idade é {idade}.')

if idade <= 9:
    print(f'CATEGORIA MIRIM')
elif idade <= 14:
    print(f'CATEGORIA INFANTIL')
elif idade <= 19:
    print(f'CATEGORIA JÚNIOR')
elif idade <= 20:
    print(f'CATEGORIA SÊNIOR')
elif idade > 20:
    print('CATEGORIA MASTER')
