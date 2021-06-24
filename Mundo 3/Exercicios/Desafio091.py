from operator import itemgetter
from random import randint
from time import sleep

r = []
j = {'Jogador 1': randint(0, 6), 'Jogador 2': randint(0, 6), 'Jogador 3': randint(0, 6), 'Jogador 4': randint(0, 6)}
for k, v in j.items():
    print(f'{k} obteve {v} no dado')
    sleep(0.5)
print('-=-' * 49)
r = sorted(j.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(r):
    print(f'{i + 1}ª Posição: {v[0]} com {v[1]}')
    sleep(0.5)
