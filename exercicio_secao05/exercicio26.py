def kml():
    consumo = int(input('Quantos km/l o carro faz?'))

    if consumo <= 8:
        print('Venda o carro!')
    elif 8 > consumo < 12:
        print('Carro econômico.')
    else:
        print('Carro super econômico')

    repetir()


def repetir():

    rep = str(input('Para repetir a pergunta digite S para sim e N para não.'))
    if rep.upper() == 'S':
        kml()
    else:
        print('Volte sempre!')


kml()