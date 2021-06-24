def voto(ano):
    from datetime import datetime
    i = datetime.today().year - ano
    if i < 16:
        print(f'Com {i} anos: VOTO NEGADO!')
    elif 65 > i >= 18:
        print(f'Com {i} anos: VOTO OBRIGATÓRIO!')
    else:
        print(f'Com {i} anos: VOTO OPCIONAL!')


voto(int(input('Em que ano você nasceu? ')))
