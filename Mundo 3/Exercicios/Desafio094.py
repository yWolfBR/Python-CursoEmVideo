pl = list()
pd = dict()
si = m = 0
linha = ('-=-' * 49)
while True:
    pd['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        s = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if s in 'FM':
            pd['sexo'] = s
            break
        else:
            print('ERRO! Responda com M ou F')
    pd['idade'] = int(input('Idade: '))
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
        else:
            print('ERRO! Responda com S ou N')
    pl.append(pd.copy())
    if c in 'N':
        break
print(linha)
print(f'Ao todo temos {len(pl)} pessoas cadastradas')
for p in pl:
    si += p['idade']
m = si / len(pl)
print(f'A média de idade do grupo é de {m:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in pl:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' > ')
print()
print('Lista de pessoas que estão com idade acima da média:')
for p in pl:
    if p['idade'] > m:
        print(f'    Nome: {p["nome"]}, Sexo: {p["sexo"]}, Idade: {p["idade"]}')
print('<<<=== ENCERRADO ===>>>')

