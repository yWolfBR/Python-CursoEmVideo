from random import shuffle

a1 = input('Aluno(a) 1: ')
a2 = input('Aluno(a) 2: ')
a3 = input('Aluno(a) 3: ')
a4 = input('Aluno(a) 4: ')
al = [a1, a2, a3, a4]
shuffle(al)
print('A ordem de apresentação será:\n{}'.format(al))
