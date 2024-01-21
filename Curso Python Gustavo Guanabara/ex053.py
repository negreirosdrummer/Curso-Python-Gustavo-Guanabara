# DESAFIO 53
# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS.
# EXEMPLOS DE PALÍNDROMOS:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

# MINHA RESOLUÇÃO:
"""frase = input('Digite uma frase qualquer: ').replace(' ', '').upper()
palindromo = ''
for c in range(len(frase) - 1, -1, -1):
    palindromo += frase[c]
if palindromo == frase:
    print(f'\nO inverso de {frase} é {palindromo}')
    print('Essa frase É PALÍNDROMO!')
elif palindromo != frase:
    print(f'\nO inverso de {frase} é {palindromo}')
    print('Essa frase NÃO É PALÍNDROMO!')


# OUTRA POSSÍVEL SOLUÇÃO:
frase = input('Digite uma frase qualquer: ').replace(' ', '').upper()
palindromo = frase[::-1]
if palindromo == frase:
    print(f'\nO inverso de {frase} é {palindromo}')
    print('Essa frase É PALÍNDROMO!')
elif palindromo != frase:
    print(f'\nO inverso de {frase} é {palindromo}')
    print('Essa frase NÃO É PALÍNDROMO!')
"""

# RESOLUÇÃO GUANABARA
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'\nO inverso de {junto} é {inverso}')
if inverso == junto:
    print('Essa frase É PALÍNDROMO!')
else:
    print('Essa frase NÃO É PALÍNDROMO!')
