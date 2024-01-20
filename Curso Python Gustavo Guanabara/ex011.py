# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE
# TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2 METROS QUADRADOS

larg = float(input('Digite a largura da parede (em metros): '))
alt = float(input('Digite a altura da parede (em metros): '))
area = larg * alt
tinta = area / 2
print(f'A área da parede é de {area}m²')
print(f'Serão necessários {tinta}L de tinta para pintar essa parede')
