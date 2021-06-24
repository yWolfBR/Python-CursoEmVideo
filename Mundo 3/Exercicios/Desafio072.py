nums = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    nd = int(input('Digite um número de 0 a 20: '))
    if 0 <= nd <= 20:
        break

print(f'O número digitado foi {nums[nd]}')
