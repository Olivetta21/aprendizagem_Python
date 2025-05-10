cig_day = int(input('Em media, quantos cigarros voce fuma por dia? '))
por_qnt_anos = float(input('Por quantos anos voce fumou? '))
acadacig = 10
qnt_vc_perdeu = ((((cig_day * 365) * por_qnt_anos) * acadacig) / 1440)
print('Voce perdeu por volta de %.f dias' % qnt_vc_perdeu)
em_ano = qnt_vc_perdeu / 365
print('Isso da entorno de %.f anos' % em_ano)
input()
