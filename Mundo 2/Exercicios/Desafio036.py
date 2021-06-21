c = float(input('Qual o valor do imóvel? R$'))
sa = float(input('Qual seu salário atual? R$'))
a = int(input('Em quantos anos você pretende pagar? '))

s = sa * (30 / 100)
vp = c / (a * 12)

if vp > s:
    print('\033[31mMás notícias. Infelizmente seu empréstimo não foi aprovado!\033[m')
else:
    print('\033[32mBoas notícias. Seu empréstimo foi aprovado!\nO valor das suas prestações será de R${:.2f}\033[m'
          .format(vp))
