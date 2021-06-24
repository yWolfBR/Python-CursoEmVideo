vl = []
vlp = []
vli = []

while True:
    vl.append(int(input('Digite um número: ')))
    while True:
        c = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
    if c in 'N':
        break
vl.sort()
for p in range(0, len(vl)):
    if vl[p] % 2 == 0:
        vlp.append(vl[p])
    else:
        vli.append(vl[p])
print('-=-' * 25)
print(f'Os valores digitados foram {vl}\nOs valores pares são {vlp}\nOs valores ímpares são {vli}')
