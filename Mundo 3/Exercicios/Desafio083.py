exp = []
e = str(input('Digite a expressão: '))
for s in e:
    if s == '(':
        exp.append('(')
    elif s == ')':
        if len(exp) > 0:
            exp.pop()
        else:
            exp.append(')')
            break
print('Sua expressão é valida' if len(exp) == 0 else 'Sua expressão é inválida')
