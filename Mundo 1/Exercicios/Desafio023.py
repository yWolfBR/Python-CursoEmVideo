n = int(input('Digite um número de 0 a 9999: '))
print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(n // 1000 % 10, n // 100 % 10, n // 10 % 10, n % 10))
