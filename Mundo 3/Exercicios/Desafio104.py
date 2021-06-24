def leiaint(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('ERRO! Digite um número inteiro')


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
