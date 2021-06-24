nl = []
for c in range(0, 5):
    nl.append(int(input(f'{c} - Digite um número: ')))
print(f'Você digitou os valores {nl}')
maior = max(nl)
menor = min(nl)
print(f'O MAIOR valor digitado foi {maior} nas posições: ', end='')
for c in range(0, 5):
    if maior == nl[c]:
        print(f'{nl.index(maior, c)},', end=' ')

print(f'\nO MENOR valor digitado foi {menor} nas posições: ', end='')
for c in range(0, 5):
    if menor == nl[c]:
        print(f'{nl.index(menor, c)},', end=' ')
