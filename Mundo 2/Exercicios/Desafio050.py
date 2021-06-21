print('Vou somar todos os números que forem pares pra você :)\nSe você digitar um número ímpar irei desconsiderá-lo')
s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = n + s
print('A soma total é de {}'.format(s))
