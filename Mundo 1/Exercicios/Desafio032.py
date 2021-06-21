print('Vamos descobrir se o ano que você pensou é BISSEXTO!')
ano = int(input('Digite aqui o ano: '))
c1 = ano % 4
c2 = ano % 100
c3 = ano % 400
print(c1, c2, c3)
if c1 == 0 and c2 != 0 or c1 == 0 and c2 == 0 and c3 == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} não é Bissexto!'.format(ano))
