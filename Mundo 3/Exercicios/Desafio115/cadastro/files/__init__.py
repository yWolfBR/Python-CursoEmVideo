def fileisreal(n):
    try:
        f = open(n, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def filebecomereal(n):
    try:
        f = open(n, 'wt+')
        f.close()
    except Exception:
        print(f'ERRO! Arquivo {n} não foi criado com sucesso')
    else:
        print(f'Arquivo {n} criado com sucesso')
    finally:
        f.close()


def fileread(n):
    try:
        f = open(n, 'rt')
    except Exception:
        print(f'ERRO ao ler o arquivo {n}')
    else:
        for line in f:
            d = line.split(';')
            d[1] = d[1].replace('\n', '')
            print(f'{d[0]:<40}{d[1]:>5} anos')
    finally:
        f.close()


def filewrire(n, nome="<Desconhecido>", idade=0):
    try:
        f = open(n, 'at+')
    except Exception:
        print(f'ERRO na abertura do arquivo {n}')
    else:
        try:
            f.write(f'{nome};{idade}\n')
        except Exception:
            print(f'ERRO na hora de escrever no arquivo {n}')
        else:
            print('Novo registro efetuado com sucesso!')
            f.close()
