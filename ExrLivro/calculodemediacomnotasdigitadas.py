qntnotas = input('Quantas notas voce quer calcular? ')
soma = 0
x = 1
while x <= int(qntnotas):
    notas = float(input(f'A nota do {x}º Bimestre: '))
    soma += notas
    x += 1
res = soma/(x-1)
print(f'Media: {res:.1f}')
if res < 6:
    if res > 3:
        print('voce esta de exame!')
    elif res > 0:
        print('Reprovado!')
    else:
        print(f'Voce ficou com {res:.0f} nota, com certeza esta reprovado!!!!')
else:
    if res < 10:
        print('Voce passou!')
    else:
        print('Voce passou com nota maxima!')
input()
