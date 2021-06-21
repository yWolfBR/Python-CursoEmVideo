d = int(input('Dias: '))
km = float(input('KM rodados: '))
'''
vd = 60 * d
vkm = km * 0.15
vt = vd + vkm
print('O valor total do seu aluguel é R${}'.format(vt))
'''
print('O valor total do seu aluguel é R${:.2f}'.format((60 * d) + (km * 0.15)))
