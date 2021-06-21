n = int(input('Digite um número inteiro: '))
b = int(input('Escolha a base para efetuar a conversão\n1-Binário\n2-Octal\n3-Hexadecimal\nSelecione aqui: '))

if b == 1:
    v = format(n, 'b')
    t = 'BINARIO'
elif b == 2:
    v = format(n, 'o')
    t = 'OCTAL'
elif b == 3:
    v = format(n, 'x')
    t = 'HEXADECIMAL'
else:
    print('A opção selecionada é inválida!')
    exit()
print('{} convertido para {} é igual a {}'.format(n, t, v))
