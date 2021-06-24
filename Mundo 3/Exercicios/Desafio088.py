from random import randint
from time import sleep

js = list()
temp = []
linha = '-=-' * 49
msg = 'MEGA SENA DO PYTHON'
print(f'''{linha}
{msg:^147}
{linha}''')
j = int(input('Quantos jogos você deseja sortear? '))
print('-=-' * 3, f'SORTEANDO {j} JOGOS', '-=-' * 3)
for c in range(0, j):
    while True:
        ns = randint(1, 60)
        if ns not in temp:
            temp.append(ns)
        if len(temp) == 6:
            break
    temp.sort()
    js.append(temp[:])
    temp.clear()
    print(f'JOGO {c + 1}: {js[c]}')
    sleep(1)
print('-=-' * 4, '<BOA SORTE>', '-=-' * 4)
