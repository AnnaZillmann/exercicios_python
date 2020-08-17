import random

acertos = 0
erros = 0

val = random.sample(range(0, 101), 2)
subt = val[0]
print(val)

a = int(input('Qual a soma dos dois valores?'))
print(f'A soma de {val} = {sum(val)}.')
if a == (sum(val)):
    acertos += 1
    print('Resposta correta.')
else:
    erros += 1
    print('Resposta errada.')

val = random.sample(range(0, 101), 2)
subt = val[0]
print(val)

b = int(input('Qual a soma dos dois valores?'))
print(f'A soma de {val} = {sum(val)}.')
if b == (sum(val)):
    acertos += 1
    print('Resposta correta.')
else:
    erros += 1
    print('Resposta errada.')

val = random.sample(range(0, 101), 2)
subt = val[0]
print(val)

c = int(input('Qual a soma dos dois valores?'))
print(f'A soma de {val} = {sum(val)}.')
if c == (sum(val)):
    acertos += 1
    print('Resposta correta.')
else:
    erros += 1
    print('Resposta incorreta.')

val = random.sample(range(0, 101), 2)
subt = val[0]
print(val)

d = int(input('Qual a soma dos dois valores?'))
if d == (sum(val)):
    acertos += 1
    print('Resposta correta.')
else:
    erros += 1
    print('Resposta errada.')

val = random.sample(range(0, 101), 2)
subt = val[0]
print(val)

e = int(input('Qual a soma dos dois valores.'))
if e == (sum(val)):
    acertos += 1
    print('Resposta correta.')
else:
    erros += 1
    print('Resposta incorreta.')

print(f'Quantidade de acertos {acertos}, quantidade de erros {erros}.')
