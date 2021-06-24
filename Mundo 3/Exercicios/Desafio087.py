linha = '-=-' * 49
print(linha)
vl = [[], [], []]
sp = sc3 = 0
for line in range(0, 3):
    for c in range(0, 3):
        vl[line].append(int(input(f'Digite um valor para [{line}, {c}]: ')))
print(linha)
for line in range(0, 3):
    for c in range(0, 3):
        print(f'[{vl[line][c]:^5}]', end=' ')
    print()
print(linha)
# SOMA DE TODOS OS VALORES PARES
for line in range(0, 3):
    for c in range(0, 3):
        if vl[line][c] % 2 == 0:
            sp += vl[line][c]
# SOMA DOS VALORES DA TERCEIRA COLUNA
for line in range(0, 3):
    sc3 += vl[line][2]
print(f'A SOMA dos valores PARES é {sp}')
print(f'A SOMA dos valores da TERCEIRA COLUNA é {sc3}')
print(f'O MAIOR valor da SEGUNDA LINHA é {max(vl[1])}')
