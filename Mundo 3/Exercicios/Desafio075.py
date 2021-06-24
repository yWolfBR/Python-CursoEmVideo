ns = (
int(input('Digite o 1º valor: ')),
int(input('Digite o 2º valor: ')),
int(input('Digite o 3º valor: ')),
int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores: {ns}\nO número 9 apareceu {ns.count(9)} vezes')
if 3 in ns:
    print(f'O primeiro número 3 apareceu na {ns.index(3) + 1}ª posição')
else:
    print('O número não foi digitado em nenhuma posição')
print('Os números pares são: ', end='')
for c in range(0, len(ns)):
    if ns[c] % 2 == 0:
        print(f'{ns[c]} ', end='')

