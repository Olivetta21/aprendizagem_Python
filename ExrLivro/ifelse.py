cat = int(input('Selecione uma categoria: '))
if cat == 1:
    preco = 12
elif cat == 2:
    preco = 23
elif cat == 3:
    preco = 34
elif cat == 4:
    preco = 45
else:
    print('Erro, selecione uma categoria de 1 - 4')
    preco = 0
print(f'o preco do produto é : {preco}')
input()
