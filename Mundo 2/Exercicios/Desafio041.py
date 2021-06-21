from datetime import date

a = int(input('Digite seu ano de nascimento: '))
aa = date.today().year
i = aa - a
if i <= 9:
    c = 'MIRIM'
elif 9 < i <= 14:
    c = 'INFANTIL'
elif 14 < i <= 19:
    c = 'JUNIOR'
elif 19 < i <= 25:
    c = 'SÊNIOR'
elif i > 25:
    c = 'MASTER'
print('Você tem {} anos e ficou na categoria \033[4m{}\033[m'.format(i, c))
