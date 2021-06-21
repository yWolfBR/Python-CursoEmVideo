v = float(input('Qual o valor total do produtos? R$'))
p = int(input('Qual a forma de pagamento?\n[1] - Á Vista dinheiro/cheque\n[2] - Á Vista no cartão\n'
              '[3] - 2x no cartão\n[4] - 3x ou mais no cartão\nSua opção: '))

if p == 0 or p > 4:
    print('Forma de pagamento invalida!')
    exit()
elif p == 4:
    pp = int(input('Quantas parcelas? '))
    vp = v + (v * (20 / 100))
    print('Nessa forma de pagamento você tem um acréscimo de 20%\nSeus produtos ficam em R${:.2f}, cada parcela será de'
          ' R${:.2f}'.format(vp, vp / pp))
elif p == 1:
    print('Nessa forma de pagamento você ganha desconto de 10%\nSeus produtos vão sair por apenas R${:.2f}'
          .format(v - (v * (10 / 100))))
elif p == 2:
    print('Nessa forma de pagamento você ganha desconto de 5%\nSeus produtos vão sair por apenas R${:.2f}'
          .format(v - (v * (5 / 100))))
elif p == 3:
    print('Nessa forma de pagamento você não ganha desconto\nSeus produtos vão sair por R${:.2f} cada parcela'
          .format(v / 2))
