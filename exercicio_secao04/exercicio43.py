produto = float(input('Informe o valor do produto vendido.'))
desconto = (produto - (produto * 0.1))
parcela = produto / 3
comissao1 = (produto - (produto - (desconto * 0.05)))
comissao2 = (produto - (produto - (produto * 0.05)))
print(f'O total a ser pago pelo produto é R$ {desconto}')
print(f'O valor a ser pago parcelado são 3 x R$ {parcela}')
print(f'A comissão do vendedor com o desconto será de R$ {comissao1}')
print(f'A comissao do vendedos sem o desconto sobre o produto é de R$ {comissao2}')

# Exercício 44

degrau = float(input('Qual a altura do degrau?'))
altura = float(input('Qual a altura a ser alcançada?'))
medida = altura // degrau  #número inteiro

print(f'A quantidade de degraus necessários para alcançar a altura de {altura} metros são, {medida} degraus.')
