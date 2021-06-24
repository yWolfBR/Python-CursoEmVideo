from random import randint


def sorteia(lst):
    lst.clear()
    for c in range(0, 5):
        lst.append(randint(1, 10))
    print(f'Os números sorteados foram {lst}')


def somapar(lst):
    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f'A soma dos valores pares de {lst} é {s}')


numeros = []

sorteia(numeros)
somapar(numeros)
