# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU ÍNDICE DE MASSA CORPORAL (IMC) E
# MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
# – IMC ABAIXO DE 18,5: ABAIXO DO PESO
# – ENTRE 18,5 E 25: PESO IDEAL
# – 25 ATÉ 30: SOBREPESO
# – 30 ATÉ 40: OBESIDADE
# – ACIMA DE 40: OBESIDADE MÓRBIDA

print('-=' * 9)
print('CALCULADORA DE IMC')
print('-=' * 9)
peso = float(input('\nInforme o peso (Kg): '))
altura = float(input('Informe a altura (m): '))
imc = peso / altura ** 2
print(f'\nO IMC é {imc:.1f}')

if imc < 18.5:
    print('Clasificação: \033[1;33mABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Clasificação: \033[1;32mPESO IDEAL')
elif 25 <= imc < 30:
    print('Clasificação: \033[1;33mSOBREPESO')
elif 30 <= imc < 40:
    print('Clasificação: \033[1;33mOBESIDADE')
elif imc >= 40:
    print('Clasificação: \033[1;31mOBESIDADE MÓRBIDA')
