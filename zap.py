from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def chamada_webdriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')
    time.sleep(4)

continuar = 'S'
contatos = []

while continuar == 'S':
    contatos.append(input("Nome: "))
    continuar = input("S - Para Continuar / N - Para parar").upper()

mensagem = input("Mensagem a ser enviada!")

def contatos(contato):

    chamada_webdriver()
    campo_pesquisa = chamada_webdriver().find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def msg(mensagem):

    campo_msg = chamada_webdriver().find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_msg[1].click()
    time.sleep(3)
    campo_msg[1].send_keys(mensagem)
    campo_msg[1].send_keys(Keys.ENTER)

for contato in contatos:
    contatos(contato)
    msg(mensagem)
