cc = 0
s = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        s = c + s
        cc = cc + 1
print('O total de soma de todos os {} números ímpares multiplos de 3 entre 1 e 500 é {}'.format(cc, s))
