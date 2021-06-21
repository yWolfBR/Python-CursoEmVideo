from random import randint

print('Vou pensar em um número de 0 a 5 e você tem que tentar adivinhar :)\nVamos começar?')
nu = int(input('Escolha um número de 0 a 5: '))
nr = randint(0, 5)
if nu >= 6:
    print('Você digitou um número maior que 5 :(')
elif nu == nr:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Eu pensei no número {}'.format(nr))
