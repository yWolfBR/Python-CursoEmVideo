plr = dict()
golsp = []
plrs = list()
linha = '-=-' * 49
linha2 = '-' * 53
cod = 0
while True:
    plr.clear()
    golsp.clear()
    plr['nome'] = str(input('Nome: ')).strip().capitalize()
    pj = int(input(f'Quantas partidas {plr["nome"]} jogou? '))
    for c in range(0, pj):
        golsp.append(int(input(f'Quantos Gols na partida {c + 1}? ')))
    plr['gols'] = golsp[:]
    plr['total'] = sum(golsp)
    plrs.append(plr.copy())
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
        print('ERRO! Use S ou N')
    if c in 'N':
        break
print(f'{linha}\n{plrs}\n{linha}')
print(f'| Cod | Nome               | Gols           | Total |\n{linha2}')
for p in enumerate(plrs):
    print(f'|{cod:>4}', end='| ')
    print(f'{plrs[cod]["nome"]:<19}', end='| ')
    print(f'{str(plrs[cod]["gols"]):<15}', end='| ')
    print(f'{plrs[cod]["total"]:<7}', end='|')
    print()
    cod += 1
print(linha2)
while True:
    b = int(input('Mostrar dados de qual jogador? [999 para finalizar]: '))
    if b == 999:
        break
    if b >= len(plrs):
        print('ERRO! Jogador não cadastrado')
    else:
        print(f'Estatística do jogador {plrs[b]["nome"]}:')
        for i, g in enumerate(plrs[b]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
print(linha)
