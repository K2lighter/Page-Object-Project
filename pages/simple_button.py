from selenium.webdriver.common.by import By
from pages.basic import BasePage


class SimpleButtonPage(BasePage):
    button_locator = (By.XPATH, '//input[@id="submit-id-submit"]')
    result_locator = (By.ID, 'result-text')
    simple_url = "https://www.qa-practice.com/elements/button/simple"

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get(self.simple_url)

    def button(self):
        return self.find(self.button_locator)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def result(self):
        return self.find(self.result_locator)
