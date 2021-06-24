def area():
    print(f'{"Controle de terrenos":^60}')
    print('-=-' * 20)
    la = float(input('Largura do terreno (m): '))
    co = float(input('Comprimento do terreno (m): '))
    print(f'A área de de um terreno de {la}*{co} tem {la * co}m²')
    print('-=-' * 20)


area()
