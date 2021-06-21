n = int(input('Digite um número para saber seu Fatorial: '))
print('Calculando {}! ='.format(n), end='')
loop = n + 1
while loop != 2:
    loop -= 1
    n = n * (loop - 1)
    print(' {} *'.format(loop), end='')
print(' 1 = {}'.format(n))
