# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS.
# A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR. NO FINAL, MOSTRE:
# QUANTAS PESSOAS TEM MAIS DE 18 ANOS
# QUANTOS HOMENS FORAM CADASTRADOS
# QUANTAS MULHERES TEM MENOS DE 20 ANOS

# MINHA RESOLUÇÃO
maiores = total_h = total_m20 = 0
while True:
    print('--' * 15)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('--' * 15)
    idade = int(input('Idade: '))
    if idade > 18:
        maiores += 1
    sexo = input('Sexo: [M/F] ').strip().upper()
    while sexo not in 'MF':
        sexo = input('Sexo inválido. Digite somente M ou F: ').strip().upper()
    if sexo == 'M':
        total_h += 1
    if sexo == 'F' and idade < 20:
        total_m20 += 1
    print('--' * 15)
    continuar = input('Cadastrar outra pessoa? [S/N] ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Digite somente S ou N: ').strip().upper()
    if continuar == 'N':
        break

print('\n====== FIM DO PROGRAMA ======')
print(f'Pessoas com mais de 18 anos: {maiores}')
print(f'Homens cadastrados: {total_h}')
print(f'Mulheres com menos de 20 anos: {total_m20}')
