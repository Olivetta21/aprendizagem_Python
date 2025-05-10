import whatsapp_api as wapi

wp = wapi.WhatsApp()

input("Pressione enter apos escanear o QR Code")

while True:
    pesq_pessoa = input("Contato: ")
    qnts = int(input("Qnts mensagens: "))
    msg_user = '     '

    wp.returnToHomePage()
    print("Pesquisando...")
    wp.search_contact(pesq_pessoa)
    while qnts > 0:
        print("Mandando mensagem...")
        wp.send_message(msg_user)
        print("Sucesso!")
        qnts -= 1
    wp.returnToHomePage()

    input("-> ")

#wp.driver.close()
