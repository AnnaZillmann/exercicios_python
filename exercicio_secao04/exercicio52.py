valor_do_premio = int(input('Qual o valor do prêmio?'))
j1 = int(input('Quanto apostou o jogador 1?'))
j2 = int(input('Quanto apostou o jogador 2?'))
j3 = int(input('Quanto apostou o jogador 3?'))

menor = j1
if j2<j1 and j2<j3:
    menor = j2
if j3<j1 and j3<j2:
    menor = j3

maior = j3
if j1>j3 and j1>j2:
    maior = j1
if j2>j3 and j2>j1:
    maior = j2

meio = j2
if j3>j1 and j3<j2:
    meio = j3
if j3<j1 and j3>j2:
    meio = j3
if j1>j2 and j1<j3:
    meio = j1
if j1<j2 and j1>j3:
    meio = j1


menor1 = (valor_do_premio * 0.2)
meio1 = (valor_do_premio * 0.3)
maior1 = (valor_do_premio * 0.5)

print(f'O jogador que apostou o menor valor, apostou R$ {menor} ganhando R$ {menor1}, o que apostou o valor médio\n apostou R$'
      f'{meio} e ganhou R$ {meio1} e o que apostou o maior valor R$ {maior} e ganhou R$ {maior1}')
