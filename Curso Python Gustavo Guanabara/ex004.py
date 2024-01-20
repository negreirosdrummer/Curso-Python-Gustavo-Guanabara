# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU
# TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE

variavel = input('Digite algo: ')
print(type(variavel))
print("É alfanumérico?", variavel.isalnum())
print("É alfabético?", variavel.isalpha())
print("É ASCII?", variavel.isascii())
print("É decimal?", variavel.isdecimal())
print("É dígito?", variavel.isdigit())
print("É identificador?", variavel.isidentifier())
print("É minúsculo?", variavel.islower())
print("É numérico?", variavel.isnumeric())
print("É imprimível?", variavel.isprintable())
print("É espaço?", variavel.isspace())
print("É maiúsculo?", variavel.isupper())
print("É capitalizada?", variavel.istitle())
