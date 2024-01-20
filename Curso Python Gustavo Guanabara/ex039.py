# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM A SUA IDADE, SE ELE AINDA
# VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA EXATA DE SE ALISTAR OU SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO

from datetime import datetime

print('-=' * 10)
print('ALISTAMENTO MILITAR')
print('-=' * 10)
sexo = ' '
while sexo not in 'MF':
    sexo = input('Informe o sexo [M/F]: ').strip().upper()

if sexo == 'F':
    print('Você não precisa se alistar no serviço militar obrigatório')
elif sexo == 'M':
    ano_nasc = int(input('Informe o ano de nascimento: '))
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc

    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')

    if idade < 18:
        if idade == 17:
            print(f'Ainda falta {18 - idade} ano para o alistamento')
            print(f'Seu alistamento será em {ano_nasc + 18}')
        elif idade != 17:
            print(f'Ainda faltam {18 - idade} anos para o alistamento')
            print(f'Seu alistamento será em {ano_nasc + 18}')
    elif idade == 18:
        print('Está na hora de se alistar!')
    elif idade > 18:
        print(f'Você deveria ter se alistado há {idade - 18} anos')
        print(f'Seu alistamento foi em {ano_nasc + 18}')
