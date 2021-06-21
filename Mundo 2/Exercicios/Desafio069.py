m = h = f = 0

while True:
    print('''{0}
 CADASTRO PIKATRON 7000
{0}'''.format('-=-' * 8))
    i = int(input('Digite a idade: '))
    s = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    while s not in 'MmFf':
        s = str(input('Sexo inválido! Tente novamente: ')).strip().upper()[0]
    if i >= 18:
        m += 1
    if s in 'Mm':
        h += 1
    if s in 'Ff' and i < 20:
        f += 1
    c = ' '
    while c not in 'SsNn':
        c = str(input('Você quer continuar cadastrando? [S/N]: ')).strip().upper()[0]
    if c in 'Nn':
        print('-=-' * 13)
        break
print(f'{m} Pessoas cadastradas são maiores de 18 anos\n{h} Homens foram cadastrados\n{f} Mulheres tem menos de 20 anos'
      f'')
