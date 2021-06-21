n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    t = 1
else:
    print('Os segmentos NÃO PODEM formar um Triângulo')
    exit()

if n1 == n2 and n1 == n3:
    print('Os segmentos podem formar um \033[4mTriângulo Equilátero\033[m')
elif n1 != n2 and n1 != n3:
    print('Os segmentos podem formar um \033[4mTriângulo Escaleno\033[m')
else:
    print('Os segmentos podem formar um \033[4mTriângulo Isósceles\033[m')
