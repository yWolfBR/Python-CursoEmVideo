n = int(input('Digite um número para saber seu Fatorial: '))
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' * ' if c > 1 else ' = ', end='')
    n = n * (c - 1)
print('{}'.format(n))
