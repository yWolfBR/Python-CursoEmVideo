vl = []
for c in range(0, 5):
    n = int(input(f'{c} - Digite um valor: '))
    if c == 0 or n > vl[-1]:
        vl.append(n)
    else:
        pos = 0
        while pos < len(vl):
            if n <= vl[pos]:
                vl.insert(pos, n)
                break
            pos += 1
print('-=-' * 25)
print(f'Os valores digitados foram {vl}')
