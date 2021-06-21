from time import sleep

while True:
    n = int(input('Digite um número positivo: '))
    if n < 0:
        break
    print('-=-' * 8)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c:2}')
    print('-=-' * 8)
    sleep(1)
print('''{0}
Obrigado por utilizar :)
{0}'''.format('-=-' * 8))
