# DESAFIO 57
# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES ‘M’ OU ‘F’.
# CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO

# MINHA RESOLUÇÃO
# sexo = input('Informe o sexo [M/F]: ').strip().upper()
# while sexo not in 'MF':
#     sexo = input('Sexo inválido, Por favor, informe seu sexo: ').strip().upper()
# print(f'Você digitou o sexo "{sexo}"')


# RESOLUÇÃO GUANABARA
sexo = input('Informe o sexo [M/F]: ').strip().upper()[0]  # [0] serve para pegar somente a primeira letra (caso seja
# digitado "Masculino", por exemplo)
while sexo not in 'MF':
    sexo = input('Sexo inválido, Por favor, informe seu sexo: ').strip().upper()
print(f'Você digitou o sexo "{sexo}"')
