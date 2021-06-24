vl = []
while True:
    n = int(input('Digite um número: '))
    if n in vl:
        print('Valor duplicado! Não será computado')
    else:
        vl.append(n)
        print('Valor computado com sucesso!')
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
    if c in 'N':
        break
print('-=-' * 15)
vl.sort()
print(f'Você digitou os valores {vl}')
