
from pages.defaultPage import Page, Component
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException

class LoginPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN_MODAL = '//*[@id="loginModal"]'
    LOGIN = '//*[@id="loginUser"]'
    PASSWORD = '//*[@id="passUser"]'
    SUBMIT = '//*[@id="sendLogin"]/input'
    LOGIN_HELLO_MSG = '//*[@id="closeInfo"]'
    LOGIN_HELLO_MSG_TITLE = '//*[@class="great_title"]'

    TRUE_HELLO_MSG = "С возвращением!"

    def get_true_hello_msg(self):
        return self.TRUE_HELLO_MSG

    def open_form(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_MODAL)
        )
        self.driver.find_element_by_xpath(self.LOGIN_MODAL).click()

    def set_login(self, login):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN)
        )
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def get_hello_msg(self):
        msg_element = WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_HELLO_MSG_TITLE)
        )
        return msg_element.get_attribute('innerText')

    def logout(self):
        self.driver.get(self.BASE_URL + 'logout')
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_MODAL)
        )
        return True
