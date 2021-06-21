print('Então você resolveu viajar! Vamos calcular o preço da sua viagem :)')
km = int(input('Quantos KM tem até o seu destino? '))
if km <= 200:
    print('O total da sua viagem será R${:.2f}'.format(km * 0.5))
else:
    print('O total da sua viagem será R${:.2f}'.format(km * 0.45))
