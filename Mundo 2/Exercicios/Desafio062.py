t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
lp = 1
lp1 = 0
mm = 10
tm = 0
while mm != 0:
    lp1 = lp1 + mm
    while lp <= lp1:
        print('{} > '.format(t), end='')
        t += r
        lp += 1
        tm += 1
    print('PAUSA')
    mm = int(input('Quantos termos a mais você deseja? '))
print('Progressão Finalizada. O total de termos mostrados foi {}'.format(tm))
