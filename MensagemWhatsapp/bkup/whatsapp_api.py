from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Parameters
WP_LINK = 'https://web.whatsapp.com'

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
        self.driver = self._setup_driver()
        self.driver.get(WP_LINK)
        print("Please scan the QR Code")

    @staticmethod
    def _setup_driver():
        ChromeDriverManager().install()
        print('Loading...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome()
        return driver

    def getElement(self, local, type = 0, times = 5):
        '''Safe get_element method with multiple attempts'''
        try:
            if type == 0:
                element = self.driver.find_element(By.XPATH, local)
            elif type == 1:
                element = self.driver.find_element(By.CLASS_NAME, local)
            #print('Found element!')
            return element
        except Exception as e:
            if times > 0:
                sleep(0.2)
                #print(f'Attempt {_count}')
                self.getElement(local, type, times - 1)
            else:
                print("Element not found")
                return 0

    def _click(self, local, type = 0):
        el = self.getElement(local, type)
        if el:
            el.click()

    def _send_keys(self, xpath, message):
        el = self.getElement(xpath)
        if el:
            el.send_keys(message)

    def write_message(self, message):
        '''Write message in the text box but not send it'''
        self._click(MESSAGE_BOX)
        self._send_keys(MESSAGE_BOX, message)

    def _paste(self):
        el = self.getElement(MESSAGE_BOX)
        if el:
            el.send_keys(Keys.SHIFT, Keys.INSERT)

    def send_message(self, message):
        '''Write and send message'''
        self.write_message(message)
        self._click(SEND)

    def get_group_numbers(self):
        '''Get phone numbers from a whatsapp group'''
        try:
            el = self.driver.find_element(By.XPATH, CONTACTS)
            return el.text.split(',')
        except Exception as e:
            print("Group header not found")

    def search_contact(self, keyword):
        '''Write and send message'''
        self._click(NEW_CHAT)
        self._send_keys(SEARCH_CONTACT, keyword)
        sleep(0.5)
        try:
            self._click(SEARCH_CLASS_NAME, 1)
        except Exception as e:
            print("Contact not found")
 
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

