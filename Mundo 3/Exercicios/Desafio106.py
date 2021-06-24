def ihelp():
    from time import sleep
    while True:
        print(f"""\033[1:30:42m{'-' * 31}
  SISTEMA DE AJUDA INTERATIVO  
{'-' * 31}""")
        h = str(input('\033[mComando ou Biblioteca: ')).strip().lower()
        if h == 'fim':
            print(f'''\033[1:41m{"-" * 12}
  ATÉ LOGO  
{"-" * 12}''')
            break
        else:
            print(f"""\033[1:30:44m{'-' * (len(h) + 34)}
  Acessando o manual do comando {h}
{'-' * (len(h) + 34)}""")
            sleep(1.5)
            print('\033[1:30:47m')
            print(f'{help(h)}\033[m')


ihelp()
