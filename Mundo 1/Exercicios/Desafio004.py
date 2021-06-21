i = input('Digite algo: ')
t = type(i)
s = (i.isspace())
n = (i.isnumeric())
a = (i.isalpha())
an = (i.isalnum())
m = (i.isupper())
mn = (i.islower())
c = (i.istitle())
print(
    'O tipo primitivo é {}\nSó tem espaços? {}\nÉ um número? {}\nÉ alfabético? {}\nÉ alfanumérico? {}\nEstá em '
    'maiúsculas? {}\nEstá em minúsculas? {}\nEstá capitalizado? {}'.format(t, s, n, a, an, m, mn, c))
