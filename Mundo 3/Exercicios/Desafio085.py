ns = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        ns[0].append(n)
    else:
        ns[1].append(n)
print('-=-' * 49)
ns[0].sort()
ns[1].sort()
print(f'Os números PARES digitados foram: {ns[0]}\nOs números ÍMPARES digitados foram: {ns[1]}')
