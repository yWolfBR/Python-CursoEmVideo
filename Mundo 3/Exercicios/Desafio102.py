def fatorial(n, show=False):
    """
    ---> Calcula o Fatorial de um número
    :param n: Número a ser calculado
    :param show: (Opcional) Mostrar ou não a conta
    """
    print('-=-' * 49)
    if show:
        print(f'{n}! =', end=' ')
        for c in range(n, 1, -1):
            print('{}'.format(c), end='')
            print(' * ' if c > 2 else ' * 1 = ', end='')
            n *= (c - 1)
    else:
        for c in range(n, 1, -1):
            n *= (c - 1)
    print(f'{n}')


help(fatorial)
fatorial(5, True)
