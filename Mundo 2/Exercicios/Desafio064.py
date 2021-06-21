s = c = 0
while True:
    n = int(input('Digite um número [999 para finalizar]: '))
    if n == 999:
        break
    else:
        s += n
        c += 1
print('Foram digitados {} números. A soma total entre eles é de {}'.format(c, s))
