from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url(*MainPageLocators.LOGIN_URL)
        self.should_be_login_form(*MainPageLocators.LOGIN_FORM)
        self.should_be_register_form(*MainPageLocators.LOGIN_FORM)

    def should_be_login_url(self):
        LOGIN_URL # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        LOGIN_FORM # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        REGISTER_FORM # реализуйте проверку, что есть форма регистрации на странице
        assert True