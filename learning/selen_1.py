# FIND ELELEMT BY ----

# https://letskodeit.teachable.com/p/practice

from selenium import webdriver

class FindByName(object):
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver  = webdriver.Chrome()
        driver.get(baseUrl)

        element1 = driver.find_element_by_id('name')
        element2 = driver.find_element_by_name('show-hide')
        element3 = driver.find_element_by_xpath('//*[@id="hide-textbox"]')
        element4 = driver.find_element_by_css_selector('#hide-textbox')
        element5 = driver.find_element_by_link_text('Login')
        element6 = driver.find_element_by_partial_link_text('Prac')
        element7 = driver.find_element_by_class_name('displayed-class')
        element8 = driver.find_element_by_tag_name('h1')


        if element1 is not None:
            print('Yo element found by id')
        else:
            print('Nothing found')
        
        if element2 is not None:
            print('Yo element found by name')
        else:
            print('Nothing found')

        if element3 is not None:
            print('Yo element found by xpath')
        else:
            print('Nothing found')

        if element4 is not None:
            print('Yo element found by css selector')
        else:
            print('Nothing found')

        if element5 is not None:
            print('Yo element found by link text')
        else:
            print('Nothing found')

        if element6 is not None:
            print('Yo element found by partial link text')
        else:
            print('Nothing found')

        if element7 is not None:
            print('Yo element found by class name')
            element7.send_keys('Yo i am just testing')
        else:
            print('Nothing found')

        if element8 is not None:
            print('Yo element found by tag name')
            print('Elment tag text : {}'.format(element8.text))
        else:
            print('Nothing found')
# find by name
ff = FindByName()
ff.test()