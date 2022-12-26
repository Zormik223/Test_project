from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def go_to_login_page(self):
        button = self.browser.find_element(By.CSS_SELECTOR, ".btn-lg")
        button.click()