def ficha(n='<Desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s)')


nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Gols: '))
if nome == '':
    nome = '<Desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
