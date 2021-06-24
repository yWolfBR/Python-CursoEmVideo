vl = []
while True:
    vl.append(int(input('Digite um número: ')))
    while True:
        c = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
    if c in 'N':
        break
vl.sort(reverse=True)
print('-=-' * 25)
print(f'Foram digitados {len(vl)} números\n{vl}')
print('O valor 5 ESTÁ na lista' if 5 in vl else 'O valor 5 NÃO ESTÁ na lista')
