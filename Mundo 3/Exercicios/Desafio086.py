linha = '-=-' * 49
vl = [[], [], []]
print(linha)
for line in range(0, 3):
    for c in range(0, 3):
        vl[line].append(int(input(f'Digite um valor para [{line}, {c}]: ')))
print(linha)
for line in range(0, 3):
    for c in range(0, 3):
        print(f'[{vl[line][c]:^5}]', end=' ')
    print()
print(linha)
