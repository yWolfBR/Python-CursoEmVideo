f = str(input('Digite aqui uma frase: ')).strip().upper().replace(' ', '').replace(',', '').replace('!', '') \
    .replace('-', '').replace('.', '').replace('?', '')
fr = f[::-1]
print('O inverso de \033[4m{}\033[m é \033[4m{}\033[m'.format(f, fr))
if f == fr:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo')
