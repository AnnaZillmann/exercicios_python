def welcome():
    print('Olá!\n')

    imposto()


def imposto():

    prod = float(input('Informe o valor do produto.'))
    est = str(input('Escolha o Estado:\n'
                    'MG para Minas Gerais\n'
                    'SP para São Paulo\n'
                    'RJ para Rio de Janeiro\n'
                    'MS para Mato Grosso do Sul\n'
                    'Opção:'))
    if est.upper() == 'MG':
        impmg = (prod * 0.07) + prod
        print(f'Valor do produto, mais o imposto é R${impmg}.')
    elif est.upper() == 'SP':
        impsp = (prod * 0.12) + prod
        print(f'Valor do produto, mais o imposto é R${impsp}.')
    elif est.upper() == 'RJ':
        imprj = (prod * 0.15) + prod
        print(f'Valor do produto, mais o imposto é R${imprj}.')
    elif est.upper() == 'MS':
        impms = (prod * 0.08) + prod
        print(f'Valor do produto, mais o imposto é R${impms}.')
    else:
        print('Dados fornecidos não compatível com os parâmetros.')

    repetir()


def repetir():
    rep = input('Quer calcular um novo produto? S para sim e N para não.')
    if rep.upper() == 'S':
        imposto()
    else:
        print('Até mais.')

welcome()