from pages.basic import BasePage
from selenium.webdriver.common.by import By

class SimpleButtonPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)