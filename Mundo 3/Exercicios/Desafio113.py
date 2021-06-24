def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido!')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar')
            return 0
        else:
            return n


def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('ERRO! Digite um número válido!')
        except KeyboardInterrupt:
            print('O usário preferiu não digitar')
            return 0
        else:
            return n


ni = leiaint('Digite um número Inteiro: ')
nf = leiafloat('Digite um número Real: ')
print(f'Você digitou o número inteiro {ni} e o número real {nf}')
