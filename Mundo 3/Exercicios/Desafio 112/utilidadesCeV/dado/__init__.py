def leiaDinheiro(txt):
    while True:
        v = str(input(txt)).strip().replace(',', '.')
        if v == '' or v.isalpha() or v.isalnum() and not v.isnumeric():
            print(f'ERRO! "{v}" não é um valor numérico válido!')
        else:
            vf = float(v)
            return vf
