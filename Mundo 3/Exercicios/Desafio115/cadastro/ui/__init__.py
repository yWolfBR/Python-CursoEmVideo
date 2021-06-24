def showline():
    return '-' * 50


def header(txt):
    print(f'{showline()}\n{txt:^50}\n{showline()}')


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


def leiastr(txt):
    t = str(input(txt)).strip()
    return t


def cmenu(lst):
    header('MENU PRINCIPAL')
    for i, v in enumerate(lst):
        print(f'{i + 1} - {v}')
    print(showline())
    return leiaint('Sua Opção: ')
