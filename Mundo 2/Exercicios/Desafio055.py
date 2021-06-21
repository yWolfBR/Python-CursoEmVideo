pm = 0
pn = 99999999999
for c in range(1, 6):
    p = float(input('Digite o {}° peso em Kg: '.format(c)))
    if p > pm:
        pm = p
    elif p < pn:
        pn = p

print('O maior peso digitado foi {:.1f}Kg\nO menor peso digitado foi {:.1f}Kg'.format(pm, pn))
