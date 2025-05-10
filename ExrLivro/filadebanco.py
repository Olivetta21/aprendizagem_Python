L = []
while True:
    fazer = input('Oque deseja fazer(add,prox,ver,pesq)? ')
    if fazer == 'pesq':
        pes = input('Pesquisar por quem? ')
        if pes == '0':
            print('Cancelado...')
        else:
            for p in L:
                if p == pes:
                    print('Ele esta na lista!')
                    break
            else:
                print('Ele nao esta na lista')
    elif fazer == 'add':
        while True:
            cliente = input('Nome do cliente (0=sair): ')
            if cliente == '0':
                break
            L.append(cliente)
    elif fazer == 'prox':
        if len(L) > 0:
            print(L.pop(0))
        else:
            print('Sem clientes para atender')
    elif fazer == 'ver':
        if len(L) == 0:
            print('Nao tem niguem na fila')
        for c in L:
            print(c)
    elif fazer == 'ok':
        break
    elif fazer == 'len':
        print(len(L))
    else:
        print('Opçoes disponiveis: add, prox, ver, pesq "ok" para sair')
input()
