hora = int(input('Qual é a hora?'))
minuto = int(input('Quantos minutos?'))
segundos = int(input('Quantos minutos?'))
dur_segundo = float(input('Quantos tempo durou em segundos?'))

hora_ajustada = ((hora * 3600) + (minuto * 60) + segundos)
tempo = hora_ajustada + dur_segundo

hora = int(tempo/3600)
if hora >= 24:
    hora = hora - 24
minutos = int((tempo % 3600)/60)
segundo = int((tempo % 3600) - minutos * 60)
if segundo >= 60:
    segundo = segundo - 60
minuto1 = int(minutos + ((segundo - 60) / 60) + 1)

print(f'{hora}:{minuto1}:{segundo}')