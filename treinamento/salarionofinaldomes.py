while True:
    PADROES = input('Modificar os padroes? s/n: ')
    if PADROES == 's':
        while True:
            cliente = int(input('Quantos clientes por dia? '))
            pqd = int(input('Por quantos dias? '))
            corte = float(input('Quanto custa um corte? '))
            salmae = float(input('Salario da mãe: '))
            pens = float(input('Pensao: '))
            alugcasa = float(input('Aluguel da casa: '))
            alugbarb = float(input('Aluguel da barbearia: '))
            agua = float(input('Agua: '))
            energia = float(input('Energia: '))
            custoad = float(input('Custo adicional: '))
            inter = float(input('Internet: '))
            salbru = cliente * corte * pqd
            junto = salbru + salmae
            aluguel = alugbarb + alugcasa
            casa = energia + agua
            despesas = aluguel + casa + custoad + pens + inter
            print(f'Salario final será: R${(junto - despesas):.2f}')
            input('')
            break
    elif PADROES == 'n':
        while True:
            cliente = int(input('Quantos clientes por dia? '))
            salmae = float(input('Salario da mãe: '))
            custoad = float(input('Custo adicional: '))
            print(f'Salario final será: R${((cliente * 25 * 26)+salmae)-(1200+600+custoad+360+250+120)}')
            input('')
            break
