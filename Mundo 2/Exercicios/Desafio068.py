from random import randint

print('''{0}
PAR ou ÍMPAR
{0}'''.format('-=-' * 4))
vc = 0
while True:
    pc = randint(0, 10)
    plr = int(input('Digite um número: '))
    pi = ' '
    while pi not in 'PpIiÍí':
        pi = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    s = pc + plr
    if s % 2 == 0:
        win = 'P'
        print(f'{pc} e {plr} = {s}. Deu PAR')
    else:
        win = 'I'
        print(f'{pc} e {plr} = {s}. Deu ÍMPAR')
    if pi in 'IiÍí':
        pi = 'I'
    if pi == win:
        print('Você venceu!')
        print('-=-' * 8)
        vc += 1
    elif pi != win:
        print('Você perdeu!')
        print('-=-' * 8)
        break
print(f'Você obteve {vc} vitórias consecutivas :)')
