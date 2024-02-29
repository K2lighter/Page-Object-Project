from selenium.webdriver.common.by import By
from time import sleep


def test_button_exist(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    assert browser.find_element(By.XPATH, '//input[@id="submit-id-submit"]').is_displayed()
    print("Button is exist, test passed")


def test_button_clickable(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    sleep(1)
    browser.find_element(By.XPATH, '//input[@id="submit-id-submit"]').click()
    print("Button is clickable, test passed")
    assert "Submitted" == browser.find_element(By.ID, 'result-text').text
    print(f"Check text = {browser.find_element(By.ID, 'result-text').text}, test passed")
