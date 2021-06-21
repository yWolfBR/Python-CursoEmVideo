from random import randint

print('{0} Vamos jogar? {0}'.format('-=-' * 3))
print('Pensei em um número de 0 a 10. Você consegue adivinhar?')
pc = randint(0, 10)
plr = ''
t = 0
while plr != pc:
    t += 1
    plr = int(input('Digite seu palpite: '))
    if plr > pc:
        print('Menor que esse, tente de novo.')
    elif plr < pc:
        print('Maior que esse, tente de novo.')
print('Você acertou com {} tentativas'.format(t))
