from random import choice

a1 = input('Aluno(a) 1: ')
a2 = input('Aluno(a) 2: ')
a3 = input('Aluno(a) 3: ')
a4 = input('Aluno(a) 4: ')
al = [a1, a2, a3, a4]
print('O aluno(a) escolhido(a) foi {}'.format(choice(al)))
