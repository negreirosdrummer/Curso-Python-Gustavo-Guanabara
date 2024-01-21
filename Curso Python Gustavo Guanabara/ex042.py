# DESAFIO 42
# REFAÇA O DESAFIO 35 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
# – EQUILÁTERO: TODOS OS LADOS IGUAIS
# – ISÓSCELES: DOIS LADOS IGUAIS, UM DIFERENTE
# – ESCALENO: TODOS OS LADOS DIFERENTES

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\nEssas retas podem formar um triângulo", end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('ISÓSCELES!')
    # é preciso escrever r3 != r1 pois r1 pode ser != de r2 e r2 pode ser != de r3, mas ainda assim o r1 pode ser = r3
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')

else:
    print("\nEssas retas não podem formar um triângulo...")
