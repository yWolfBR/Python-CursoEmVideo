tot = o1k = pmb = 0
nmb = ''
print('''{0}
  LOJA DO PYTHON
{0}'''.format('-=-' * 6))
while True:
    np = str(input('Digite o nome do produto: ')).strip().title()
    pp = float(input('Digite o valor do produto R$'))
    if nmb == '':
        pmb = pp
        nmb = np
    if pmb > pp:
        pmb = pp
        nmb = np
    tot += pp
    if pp >= 1000:
        o1k += 1
    c = ' '
    while c not in 'SsNn':
        c = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if c in 'N':
        print('-=-' * 10)
        break
print(f'O total da sua compra foi R${tot:.2f}\n{o1k} produtos custam mais de RS$1000\nO produto mais barato é {nmb} '
      f'custando R${pmb:.2f}')
