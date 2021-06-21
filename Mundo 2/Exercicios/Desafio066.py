s = d = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    s += n
    d += 1
print(f'Foram digitados {d} números. A soma total entre eles é de {s}')
