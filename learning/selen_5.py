# Click and type on a web element.

from selenium import webdriver
from selenium.webdriver.common.by import By

class ClickAndWrite(object):
    def test(self):
        driver = webdriver.Chrome()
        driver.get('https://letskodeit.teachable.com/')

        login_link = driver.find_element(By.XPATH, '//*[@id="navbar"]//a[@href="/sign_in"]')
        login_link.click()

        current_url = driver.current_url
        print(current_url)

        # driver.find_element(By.XPATH, '//*[@id="user_email"]').send_keys("TheMrinalSinha")
        # driver.find_element(By.XPATH, '//*[@id="user_password"]').send_keys('password')

xx = ClickAndWrite()
xx.test()