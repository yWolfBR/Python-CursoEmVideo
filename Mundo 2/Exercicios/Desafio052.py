vf = 0
n = int(input('Digite um número: '))
if n > 1:
    for c in range(2, n):
        if (n % c) == 0:
            vf = 1
else:
    print('Digite um número maior que 1')
    exit()

if vf == 1:
    print('O Número {} NÃO É PRIMO'.format(n))
else:
    print('O Número {} É PRIMO'.format(n))
