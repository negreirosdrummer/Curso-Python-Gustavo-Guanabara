# DESAFIO 54
# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS.
# NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES

from datetime import datetime

ano_atual = datetime.now().year
maiores = 0
menores = 0

for c in range(0, 7):
    ano_nasc = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    print(f'A pessoa {c+1} tem {ano_atual - ano_nasc} anos\n')
    if ano_atual - ano_nasc >= 21:
        maiores += 1
    else:
        menores += 1

print(f'Pessoas maiores de idade: {maiores}')
print(f'Pessoas menores de idade: {menores}')
