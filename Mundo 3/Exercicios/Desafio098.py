from time import sleep


def contador(i, f, p):
    print(f'{"-=-" * 49}')
    if p == 0:
        p += 1
    if p < 0:
        p = -p
    if i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM')
    elif i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM')
    print('-=-' * 49)


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar a contagem :)')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
