from random import randint

ns = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram : {ns}')
print(f'Maior: {max(ns)}\nMenor: {min(ns)}')
