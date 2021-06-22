n = int(input('Digite um número para saber seu Fatorial: '))
print('Calculando {}! = '.format(n), end='')
for c in range(n, 1, -1):
    print('{}'.format(c), end='')
    print(' * ' if c > 2 else ' * 1 = ', end='')
    n = n * (c - 1)
print('{}'.format(n))
