imf = 0
im = 0
si = 0
for c in range(1, 5):
    n = str(input('Digite o {}° nome: '.format(c))).strip()
    id = int(input('Digite a idade da {}° pessoa: '.format(c)))
    s = str(input('Digite o sexo da {}° pessoa: '.format(c))).strip().lower()
    si = si + id
    if s == 'masculino' and id > im:
        im = id
        nm = n
    elif s == 'feminino' and id < 20:
        imf = imf + 1
    elif s != 'masculino' and s != 'feminino':
        print('Sexo inválido!')
        exit()

print('A média de idade do grupo é {:.1f}'.format(si / 4))
print('O nome do homem mais velho do grupo é {} e sua idade é {}'.format(nm, im))
print('{} Mulheres do grupo tem menos de 20 anos'.format(imf))
