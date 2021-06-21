from random import randint

print('Vamos jogar Pedra, Papel ou Tesoura? Aposto que você não consegue me vencer ;)')
plr = str(input('Escolha: Pedra, Papel ou Tesoura? ')).strip().lower().replace(' ', '')
pc = randint(1, 3)
# processar escolha do jogador em números
if plr == 'pedra':
    plr = 1
elif plr == 'papel':
    plr = 2
elif plr == 'tesoura':
    plr = 3
else:
    print('Isso não existe no jogo :(')
    exit()
# processar se o jogador ganhou ou perdeu
if plr == pc:
    win = 0
elif plr == 1 and pc == 3 or plr == 2 and pc == 1 or plr == 3 and pc == 2:
    win = 1
else:
    win = 2
# processar escolha do pc em palavras
if pc == 1:
    pc = 'Pedra'
elif pc == 2:
    pc = 'Papel'
else:
    pc = 'Tesoura'
# mostrar na tela se ganhou ou perdeu
if win == 1:
    print('\033[32mParabéns! Você conseguiu me vencer, eu escolhi {} :(\033[m'.format(pc))
elif win == 2:
    print('\033[31mGANHEI! Eu escolhi {} ;)\033[m'.format(pc))
else:
    print('\033[36mEMPATE! Parece que você e eu pensamos da mesma forma\033[m')
