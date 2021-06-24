import moeda

n = float(input('Digite o valor R$'))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n, 10)}')
print(f'Diminuindo 15%, temos R${moeda.diminuir(n, 15)}')
