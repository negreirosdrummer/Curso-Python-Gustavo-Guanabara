# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

velocidade = int(input('Digite a velocidade atual do carro (Km/h): '))
if velocidade > 80:
    print(f'\nMULTADO! Você excedeu o limite de 80Km/h\nValor da multa: R${(velocidade - 80) * 7:.2f}')
print('Tenha um bom dia! Dirija com segurança')
