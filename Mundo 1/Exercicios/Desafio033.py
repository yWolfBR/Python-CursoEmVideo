n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
print('')
if n1 > n2 and n1 > n3:
    print('Maior: {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('Maior: {}'.format(n2))
else:
    print('Maior: {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('Menor: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('Menor: {}'.format(n2))
else:
    print('Menor: {}'.format(n3))
