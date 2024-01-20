# DESAFIO 26
# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE QUANTAS VEZES APARECE A LETRA "A", EM QUE POSIÇÃO ELA
# APARECE A PRIMEIRA VEZ E EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

frase = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes nessa frase')
print(f'Ela aparece pela primeira vez na posição {frase.find("A") + 1}')
print(f'Ela aparece pela última vez na posição {frase.rfind("A") + 1}')
