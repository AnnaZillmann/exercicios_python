x = int(input('Informe o valor de x.'))
y = int(input('Informe o valor de y.'))
z = int(input('Informe o valor de z.'))

media = input('Infome qual média deseja calcular:\n'
              'G = Geométrica\n'
              'P = Ponderada\n'
              'H = Harmônica\n'
              'A = Aritmética\n'
              'Opção:')
if media == 'G':
    mediag = ((x * y * z) ** 0.3)
    print(f'{mediag:.2f}')
elif media == 'P':
    mediap = (((x + 2) * (x + 3) * z) / 6)
    print(f'{mediap:.2f}')
elif media == 'H':
    mediah = (1 / (1/x + 1/y + 1/z))
    print(f'{mediah:.2f}')
elif media == 'A':
    mediaa = ((x + y + z) / 3)
    print(f'{mediaa:.2f}')
else:
    print('Média solicitada não localizada, favor rever informação digitada.')