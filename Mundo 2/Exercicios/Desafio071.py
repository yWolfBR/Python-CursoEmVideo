s = int(input('Qual valor de saque? NÃO CONTABILIZAMOS CENTAVOS!\nR$'))
n50 = s // 50
v50 = n50 * 50
s -= n50 * 50
n20 = s // 20
v20 = n20 * 20
s -= n20 * 20
n10 = s // 10
v10 = n10 * 10
s -= n10 * 10
n1 = s
print('-=-' * 15)
print(f'NOTAS A SEREM ENTREGUES!'.center(45))
if n50 > 0:
    print(f'{n50} NOTAS DE R$50 TOTALIZANDO R${v50}'.center(45))
if n20 > 0:
    print(f'{n20} NOTAS DE R$20 TOTALIZANDO R${v20}'.center(45))
if n10 > 0:
    print(f'{n10} NOTAS DE R$10 TOTALIZANDO R${v10}'.center(45))
if n1 > 0:
    print(f'{n1} NOTAS DE R$1 TOTALIZANDO R${n1}'.center(45))
print('-=-' * 15)
