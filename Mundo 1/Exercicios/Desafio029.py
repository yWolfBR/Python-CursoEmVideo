print('Estamos chegando um radar de velocidade!')
v = int(input('Qual a velocidade do seu carro? '))
if v > 80:
    print('Você acaba de ser multado em R${:.2f} por estar {}KM acima do limite da via!'.format((v - 80) * 7, v - 80))
else:
    print('Você estava dentro do limite de velocidade da via e não fui multado :)')
