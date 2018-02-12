# FIND ELEMENT METHOD...

from selenium import webdriver
from selenium.webdriver.common.by import By

# ID                = 'id'
# XPATH             = 'xpath'
# LINK_TEXT         = 'link_text'
# PARTIAL_LINK_TEXT = 'partial_link_text'
# NAME              = 'name'
# TAG_NAME          = 'tag_name'
# CLASS_NAME        = 'class_name'
# CSS_SELECTOR      = 'css_selector'

class FindElement(object):
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver  = webdriver.Chrome()
        driver.get(baseUrl)

        element1 = driver.find_element(By.ID, 'name')
        element2 = driver.find_element(By.NAME, 'show-hide')

        if element1 is not None:
            print('Yo element found by id')
        else:
            print('Nothing found')
        
        if element2 is not None:
            print('Yo element found by name')
        else:
            print('Nothing found')

# find element
ff = FindElement()
ff.test()