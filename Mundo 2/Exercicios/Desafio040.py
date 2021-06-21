n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2
if m < 5:
    print('Você está com média {:.2f} e foi \033[4mREPROVADO\033[m!'.format(m))
elif m >= 7:
    print('Você está com média {:.2f} e foi \033[4mAPROVADO\033[m, Parabéns!'.format(m))
else:
    print('Você está com média {:.2f} e ficou de \033[4mRECUPERAÇÃO\033[m, Estude mais!'.format(m))
