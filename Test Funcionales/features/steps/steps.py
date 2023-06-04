from behave import given,when,then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

@when(u'we visit "{browser_page}"')
def step(context, browser_page):
   context.browser.get(f"{browser_page}")

@then('it should have a title "{browser_title}"')
def step(context, browser_title ):
    assert context.browser.title == f"{browser_title}"

@when(u'we search "{article}"')
def step_impl(context, article):
   art = context.browser.find_element(By.CLASS_NAME, 'dia-search__bar')
   art.send_keys(f'{article}')
   art.send_keys(Keys.ENTER)

@then(u'it should be "{total}" articles')
def step_impl(context, total):
   sleep(3)
   articulos = context.browser.find_elements(By.CLASS_NAME, 'search-product-card-list__item-container')
   num_art = len(articulos)
   assert num_art == int(total)

@when(u'we add "item" to shopping cart')
def step_impl(context):
   context.browser.find_element(By.CLASS_NAME, 'search-product-card__top-section-content').click()
   context.browser.find_element(By.CLASS_NAME, 'add-2-cart__basic-button--enabled').click()
   sleep(3)
   context.browser.find_element(By.CLASS_NAME, 'dia-icon-clear').click()
   context.browser.get('https://www.dia.es/cart')

@then(u'there should be "{product_add}"')
def step_impl(context, product_add):
   assert context.browser.find_element(By.CLASS_NAME,'total-quantity').text == f"{product_add}"
