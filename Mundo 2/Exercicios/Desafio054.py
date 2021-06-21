from datetime import date

maior = 0
menor = 0
hj = date.today().year
for c in range(0, 7):
    d = int(input('Digite aqui o ano de nascimento: '))
    if hj - d >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print('CONSIDERANDO 21 ANOS COMO MAIORIDADE:\n{} PESSOAS SÃO MAIORES DE IDADE E {} PESSOAS SÃO MENORES DE IDADE'
      .format(maior, menor))
