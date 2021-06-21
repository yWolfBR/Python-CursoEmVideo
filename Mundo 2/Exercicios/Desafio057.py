r = 0
while r == 0:
    s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if s == 'M' or s == 'F':
        r = 1
        print('Sexo {} registrado com sucesso!'.format(s))
    else:
        print('Dado inválido! Tente novamente.')
