p = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila',
     120.32, 'Canetas', 22.30, 'Livro', 34.90)

linha = '-=-' * 15
print(linha)
print(f'{" Loja do Python ":^45}')
print(linha)
for c in range(0, len(p), 2):
    print(f'{p[c]:.<35}R${p[c + 1]:>8.2f}')
print(linha)
