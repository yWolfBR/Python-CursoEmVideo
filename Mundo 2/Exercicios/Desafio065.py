m = s = mn = mm = 0
while True:
    n = int(input('Digite um número: '))
    m += 1
    s += n
    if mn == 0 and mm == 0:
        mn = mm = n
    if mn > n:
        mn = n
    if mm < n:
        mm = n
    c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if c in 'N':
        break
print('Foram digitados {} números. A média total foi de {:.2f}'.format(m, s / m))
print('O MAIOR valor digitado foi {}\nO MENOR valor digitado foi {}'.format(mm, mn))
