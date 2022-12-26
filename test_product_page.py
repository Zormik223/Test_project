from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

def click_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()