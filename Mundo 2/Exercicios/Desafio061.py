t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
lp = 0
while lp < 10:
    print('{}'.format(t), end='')
    print(' > ' if lp < 9 else '', end='')
    t += r
    lp += 1
