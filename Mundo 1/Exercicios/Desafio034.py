s = float(input('Digite seu salário atual: R$'))
if s > 1250.00:
    print('Você recebe-rá um aumento de 10% e seu salário será R${:.2f}'.format(s + s * (10 / 100)))
else:
    print('Você recebe-rá um aumento de 15% e seu salário será R${:.2f}'.format(s + s * (15 / 100)))
