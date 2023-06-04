from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://www.dia.es/')
    sleep(3) # Esperar 3s para que aparezcan las cokkies
    context.browser.find_element(By.ID, 'onetrust-accept-btn-handler').click()

def after_all(context):
    context.browser.quit()
