n = str(input('Digite seu nome completo: ')).strip()
nl = n.split()
print('Primeiro nome: {}\nÚltimo nome: {}'.format(nl[0], nl[len(nl) - 1]))
