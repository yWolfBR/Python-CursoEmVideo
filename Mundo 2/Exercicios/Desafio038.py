n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

if n1 == n2:
    print('Ambos são \033[4mIGUAIS\033[m')
elif n1 > n2:
    print('O \033[4mPRIMEIRO\033[m valor é o maior')
else:
    print('O \033[4mSEGUNDO\033[m valor é o maior')
