tabela = ('Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Atlético-MG', 'Bragantino', 'Fluminense', 'Bahia',
          'Palmeiras', 'Corinthians', 'Ceará SC', 'Santos', 'Internacional', 'Juventude', 'Cuiabá', 'Sport Recife',
          'São Paulo', 'Chapecoense', 'Grêmio', 'América-MG')
linha = '-=-' * 98
print(linha)
print(f'Lista de times: {tabela}')
print(linha)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print(linha)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print(linha)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(linha)
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')
print(linha)
