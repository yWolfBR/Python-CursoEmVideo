nums = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    nd = int(input('Digite um número de 0 a 20: '))
    if 0 <= nd <= 20:
        print(f'O número digitado foi {nums[nd]}')
    while True:
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if c in 'SN':
            break
    if c in 'N':
        break
