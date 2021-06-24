from time import sleep


def maior(*lst):
    print(f'{"-=-" * 20}\nAnalisando os valores passados...')
    for v in lst:
        sleep(0.5)
        print(v, end=' ')
    sleep(0.5)
    print(f'Foram informados {len(lst)} valores ao todo\nO maior valor informado foi {max(lst)}\n{"-=-" * 20}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior(-1, -2, -3, -4, -5)
