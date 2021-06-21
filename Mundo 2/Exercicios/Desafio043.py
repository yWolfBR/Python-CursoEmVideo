p = float(input('Qual seu peso? Kg: '))
a = float(input('Qual sua altura? m: '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}. Você está Abaixo do seu Peso Ideal'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f}. Você está na faixa de Peso Ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}. Você está com Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}. Você está com Obesidade'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f}. Você está com Obesidade Mórbida'.format(imc))
