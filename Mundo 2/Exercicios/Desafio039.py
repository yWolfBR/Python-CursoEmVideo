from datetime import date

aa = date.today().year
i = int(input('Digite seu ano de nascimento: '))
c = aa - i
if c == 18:
    print('Você deve se alistar \033[4mESSE ANO\033[m!')
elif c < 18:
    print('Seu alistamento será em \033[4m{}\033[m!'.format(18 - c + aa))
else:
    print('Você deveria ter se alistado em \033[4m{}\033[m!'.format(aa - ((aa - i) - 18)))
