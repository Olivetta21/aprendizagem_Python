import whatsapp_api as wapi

wp = wapi.WhatsApp()

numeros = ['67 9602-1942',
    '67 9834-6078',
    '67 9903-9235',
    '67 9683-5071',
    '67 9815-7130',
    '67 8443-4919',
    '67 9664-6985',
    '67 9692-8316',
    '67 9609-9462',
    '67 9622-9987',
    '67 9697-8022',
    '67 9868-4270',
    '67 8445-4827',
    '67 9854-3226',
    '67 9806-4078',
    '67 8409-3997',
    '67 9952-4881',
    '67 9957-3847',
    '67 9800-1295']
nomes = ['ivan',
    'ilenir',
    'wiliam',
    'celina',
    'kelvin',
    'mae',
    'rafael',
    'matheus',
    'vera',
    'juliana',
    'voIda',
    'welliton',
    'kaiog',
    'kamilly',
    'edivan',
    'bruno',
    'guilherme',
    'caiod',
    'duda']
    
input("Iniciar")

for nome, numb in zip(nomes,numeros):
    msg_user = f"{nome} ignore, isso e apenas um teste"
    wp.returnToHomePage()
    if not wp.textToThisContact(msg_user, numb):
        print(f"Nao foi possivel enviar mensagem para {nome}!")
        
input("Finalizar")


#wp.driver.close()
