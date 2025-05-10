sair = input('"Conte até" n para cancelar... ')
while True:
    if sair == 'n':
        break
    limite = int(input('Limite: '))
    mult = int(input('Multiplicador: '))
    x = 0
    while x < limite:
        print(x)
        x = x + mult
    while x >= 0:
        print(x)
        x = x - mult
    continuar = input('Repetir? s/n: ')
    if continuar == 'n':
        break
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
sair = input('"Medias" n para cancelar... ')
while True:
    if sair == 'n':
        break
    x = 1
    soma = 0
    while x <= 5:
        n = int(input(f'{x}-Digite um numero: '))
        soma = soma + n
        x = x + 1
    print(f'Media: {soma/5}')
    continuar = input('Repetir? s/n: ')
    if continuar == 'n':
        break
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
sair = input('"Somador" n para cancelar... ')
while True:
    if sair == 'n':
        break
    s = 0
    while True:
        v = input('Digite um numero a somar, digite "ok" para finalizar: ')
        if v == 'ok':
            break
        s = s + int(v)
        '''observer que aqui eu coloquei int(v) porque eu precisava que o programa
        terminasse digitando ok, mas se eu deixasse em int no input "v" eu nao poderia
        digitar ok ja que ele é uma string'''

    print(f'Resultado={s}')
    continuar = input('Repetir? s/n: ')
    if continuar == 'n':
        break
print('')
input('Enter para sair...')
