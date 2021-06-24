d = list()
pp = list()
mm = mn = 0
while True:
    d.append(str(input('Nome: ')).strip().capitalize())
    d.append(float(input('Peso: ')))
    if len(pp) == 0:
        mm = mn = d[1]
    else:
        if d[1] > mm:
            mm = d[1]
        elif d[1] < mn:
            mn = d[1]
    pp.append(d[:])
    d.clear()
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
    if c in 'N':
        break
print('-=-' * 25)
print(f'Foram cadastradas {len(pp)} pessoas')
print(f'O MAIOR peso cadastrado foi {mm:.1f}Kg > ', end='')
for p in pp:
    if p[1] == mm:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O MENOR peso cadastrado foi {mn:.1f}Kg > ', end='')
for p in pp:
    if p[1] == mn:
        print(f'[{p[0]}]', end=' ')
print()
