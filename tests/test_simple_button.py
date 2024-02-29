from pages.simple_button import SimpleButtonPage


def test_button_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()
    print("Button is exist, test passed")


# def test_button_clickable(browser):
#     browser.get("https://www.qa-practice.com/elements/button/simple")
#     wait = WebDriverWait(browser, 15, poll_frequency=1)
#     button_locator = ("xpath", '//input[@id="submit-id-submit"]')
#     button_1 = (wait.until(EC.visibility_of_element_located(button_locator)))
#     button_1.click()
#     print("Button is clickable, test passed")
#     assert "Submitted" == browser.find_element(By.ID, 'result-text').text
#     print(f"Check text = {browser.find_element(By.ID, 'result-text').text}, test passed")
