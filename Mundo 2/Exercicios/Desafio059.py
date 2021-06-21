n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
ex = False
while not ex:
    print('''{0}
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA
{0}'''.format('-=-' * 8))
    o = int(input('Qual sua opção? '))
    if o == 0 or o > 5:
        print('Opção inválida!')
    else:
        if o == 1:
            print('{} {} + {} = {}'.format('>' * 5, n1, n2, n1 + n2))
        elif o == 2:
            print('{} {} * {} = {}'.format('>' * 5, n1, n2, n1 * n2))
        elif o == 3:
            if n1 > n2:
                print('Entre {} e {}, o maior é {}'.format(n1, n2, n1))
            else:
                print('Entre {} e {}, o maior é {}'.format(n1, n2, n2))
        elif o == 4:
            n1 = int(input('Digite o 1° número: '))
            n2 = int(input('Digite o 2° número: '))
        elif o == 5:
            print('Obrigado por utilizar :)')
            ex = True
