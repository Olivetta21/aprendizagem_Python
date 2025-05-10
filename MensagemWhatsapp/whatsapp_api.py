from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Parameters
WP_LINK = 'https://web.whatsapp.com'
ADDNEWCONTNUMBER = '67 9602-1942'
GOOGLEOPTIONS = ""#'C:/Users/i/AppData/Local/Google/Chrome/User Data'


## XPATHS
##CONTACTS = '//*[@id="main"]/header/div[2]/div[2]/span'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
SEND = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
NEW_CHAT = '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span'
##FIRST_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div'
SEARCH_CONTACT = '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p'
SEARCH_CLASS_NAME = '_8nE1Y'



class WhatsApp:
    def __init__(self):
        self.thisVersion = 4
        self.driver = self._setup_driver(self)
        self.driver.get(WP_LINK)
        print("Waiting for you to scan the qr code...")
        scanned = None
        while scanned == None:
            try:
                scanned = self.driver.find_element(By.CLASS_NAME, SEARCH_CLASS_NAME)
            except Exception:
                scanned = None
        print("\n\nOk, you can use the WhatsApp now!\n\n\n")

    @staticmethod
    def _setup_driver(self):
        print(f'Loading version {self.thisVersion}...')
        option = None
        if GOOGLEOPTIONS:
            option = webdriver.ChromeOptions()
            option.add_argument(f"user-data-dir={GOOGLEOPTIONS}")
        driver = webdriver.Chrome(option)
        return driver

    def getElement(self, local, type = 0):
        times = 5
        while times > 0:
            try:
                if type == 0:
                    element = self.driver.find_element(By.XPATH, local)
                elif type == 1:
                    element = self.driver.find_element(By.CLASS_NAME, local)
                return element
            except Exception:
                print(f'Attempt {times}')
                sleep(0.5)
            times -= 1
        print("Element not found")
        return None

    def _click(self, local, type = 0):
        el = self.getElement(local, type)
        if not el:
            print("Path of click not found!")
            return False
        else:
            try:
                el.click()
            except Exception:
                print("Element not clickable!")
                return False
        return True

    def _send_keys(self, xpath, message):
        el = self.getElement(xpath)
        if not el:
            print("Path of send keys not found!")
            return False
        else:
            try:
                el.send_keys(message)
            except Exception:
                print("Element not accept messages!")
                return False
        return True

    def write_message(self, message):
        if (message.isspace()):
            print("Message cant be an space!")
            return False
        if not self._send_keys(MESSAGE_BOX, message):
            print("Error in writing text!")
            return False
        return True

    def _paste(self):
        el = self.getElement(MESSAGE_BOX)
        if el:
            el.send_keys(Keys.SHIFT, Keys.INSERT)

    def send_message(self, message):
        if not self.write_message(message):
            print("Error in write message!")
            return False
        if not self._click(SEND):
            print("Send Box not found!")
            return False
        return True

    def get_group_numbers(self):
        '''Get phone numbers from a whatsapp group'''
        try:
            el = self.driver.find_element(By.XPATH, 'CONTACTS')
            return el.text.split(',')
        except Exception:
            print("Group header not found")

    def search_contact(self, keyword):
        self.driver.find_element(By.XPATH, '/html').send_keys(Keys.CONTROL, Keys.ALT, 'n')
        #if not self._click(NEW_CHAT):
        #    print("New chat Box not found!")
        #    return False
        if self._send_keys(SEARCH_CONTACT, keyword):
            print("Atraso para debug...")
            sleep(0.5)
            if not self._click(SEARCH_CLASS_NAME, 1):
                print("Contact not found")
                return False
        else:
            print("Search Contact Box not found!")
            return False
        return True
    
    def textToThisContact(self, message, contact, times = 1):
        if (len(contact) < 12):
            print("Maybe this isnt a number...")
            return False
        if self.search_contact(contact):
            while times > 0:
                if self.send_message(message):
                    print("Delivered")
                else:
                    print(f"Cant type this message: {message}")
                    return False
                times -= 1
        else:
            print(f"Cant find this contact: {contact}")
            return False
        return True
    
    def textToNonContact(self, message, number, times = 1):
        if not self.textToThisContact(number, ADDNEWCONTNUMBER):
            print("Message for the test number not send")
            return False
        self.driver.find_elements(By.XPATH, '//span[contains(@style,' + number + ')]').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/li[1]/div').click()
        self.write_message(message)
        return True
        
    
 
    def get_all_messages(self):
        all_messages_element = self.driver.find_elements(By.CLASS_NAME, '_21Ahp')
        all_messages_text = [e.text for e in all_messages_element]
        return all_messages_text

    def get_last_message(self):
        all_messages = self.get_all_messages()
        return all_messages[-1]
    
    def returnToHomePage(self, times = 5):
        htmlPage = self.driver.find_element(By.XPATH, '/html')
        while times > 0:            
            htmlPage.send_keys(Keys.ESCAPE)
            times -= 1
            

