a = list()
temp = []
while True:
    temp.append(str(input('Nome: ').strip().capitalize()))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    a.append(temp[:])
    temp.clear()
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
    if c in 'N':
        break
print('-=-' * 49)
print('No. NOME             MÉDIA\n' + '-' * 26)
for na in range(0, len(a)):
    print(f'{na:<3}', end=' ')
    print(f'{a[na][0]:<16}', end=' ')
    m = (a[na][1] + a[na][2]) / 2
    print(f'{m:>5.1f}')
print('-' * 147)
while True:
    ma = int(input('Mostrar notas de qual aluno? [999 PARA FINALIZAR]: '))
    while True:
        if ma == 999:
            break
        elif ma >= len(a):
            print('-' * 147)
            ma = int(input('ESSE ALUNO NÃO ESTÁ CADASTRADO!\nMostrar notas de qual aluno? [999 PARA FINALIZAR]: '))
        else:
            break
    if ma == 999:
        break
    else:
        print(f'As notas de {a[ma][0]} são {a[ma][1]} e {a[ma][2]}')
        print('-' * 147)
print('-' * 147)
print('OBRIGADO POR UTILIZAR :)')
