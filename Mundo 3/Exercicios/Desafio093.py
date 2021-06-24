plr = dict()
golsp = []
linha = '-=-' * 49
plr['nome'] = str(input('Nome: ')).strip().capitalize()
pj = int(input(f'Quantas partidas {plr["nome"]} jogou? '))
for c in range(0, pj):
    golsp.append(int(input(f'Quantos Gols na partida {c + 1}? ')))
plr['gols'] = golsp[:]
plr['total'] = sum(golsp)
print(f'{linha}\n{plr}\n{linha}')
for k, v in plr.items():
    print(f'{k.capitalize()}: {v}')
print(linha + f'\nO Jogador {plr["nome"]} jogou {len(plr["gols"])} partidas')
for p, g in enumerate(plr['gols']):
    print(f'Na partida {p + 1}, fez {g} gols')
print(f'Total de {plr["total"]} gols')
