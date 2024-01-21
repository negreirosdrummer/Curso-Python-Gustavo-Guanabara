# DESAFIO 40
# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA
# MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
# – MÉDIA ABAIXO DE 5.0: REPROVADO
# – MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# – MÉDIA 7.0 OU SUPERIOR: APROVADO

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2

print(f'\nA média do aluno foi {media}\nSituação do aluno:')
if media < 5:
    print('\033[1;31mREPROVADO')
elif 5 <= media < 7:
    print('\033[1;33mRECUPERAÇÃO')
elif media >= 7:
    print('\033[1;32mAPROVADO!')
