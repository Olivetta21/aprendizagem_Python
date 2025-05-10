a = input('seu nome: ')
if a == 'ivan':
    print('Senhor das galaxias seu irmao é o kelvin né?')
elif a == 'kelvin':         #elif é tipo um else misturado com if
    print('kelvinha, seu irmao é o senhor das galaxias que maneiro!')
else:
    print(f'sei la quem é {a}')
i = (input(f'{a} quantos anos voce tem? '))  #int serve apenas para numeros inteiros













print(f'o nome ({a}) vezes o numero do seu aniversario que é {i} fica: ' + a * int(i))  #tem que colocar o int porque nao pode ser um numero quebrado
