while True:
    QsCcL = int(input('Quantos seu caminhao consegue levar?(em kilos) '))
    QkUsT = int(input('Quantos kilos um saco tem?(em kilos) '))
    QvUs = float(input('Quantos vale um saco? '))
    QvVvFpD = int(input('Quantas viagens você vai fazer por dia? '))
    PqDeUm = int(input('Por quantos dias em um mês? '))
    res = (((QsCcL / QkUsT) * QvUs) * QvVvFpD) * PqDeUm
    print(f'Seu caminhao consegue levar {QsCcL / QkUsT:.2f} sacos')
    print(f'Se cada saco vale R${QvUs} então você ganha {QvUs * (QsCcL / QkUsT):.2f} por viagem')
    print(f'Se você faz {QvVvFpD} viagens por dia, ganhará R${QvVvFpD * (QvUs * (QsCcL / QkUsT)):.2f}/dia')
    print(f'Que dá em torno de R${res:.2f} por mês trabalhando {PqDeUm} dias.')
    print('')
    ta = input('Tentar de novo? s/n: ')
    if ta == 'n':
        break
