c = int(input('Informe o comprimento .'))
l = int(input('Informe a largura .'))
valor = int(input('Qual o valor do metro da tela ?'))

metro = (2 * l) + (2 * c)
pag = metro * valor

print(f'O valor para cercar a área informada é R$ {pag}.')
