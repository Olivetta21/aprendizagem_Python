print('Bom Dia!')
print('Deseja saber quantos tera que pagar de imposto para saude?')
nome = input('Primeiramente qual seu nome? ')
salario = int(input(f'{nome} quantos voce recebe por mês? '))
idade = int(input('Certo, e qual sua idade? '))
imposto_sus = 1200
juros = 100
a_cada_juros_ = 30
idade_minima = 30
quantos_por_idade = 2
if salario > 1200:
    imp_salario = ((salario - imposto_sus) / juros) * a_cada_juros_
    if idade > 30:
        imp_idade = (idade - idade_minima) * quantos_por_idade
        print('O seu imposto é', imp_salario + imp_idade)
    else:
        print('Voce precia ter no minimo 31 anos')
else:
    print('Voce precisa ter um salario acima de 1200')
input()
