# Browser Interaction and Navigating Webpages.
# Working with elements.

from selenium import webdriver

class BrowserInteractions(object):
    def test(self):
        driver = webdriver.Chrome()

        # Maximize window
        driver.maximize_window()

        # Open url
        driver.get('https://letskodeit.teachable.com/p/practice')

        # Getting Title
        title = driver.title
        print('Title of the webpage is : %s' % title)

        # Getting current url
        currUrl = driver.current_url
        print('Current url of the site is : %s' % currUrl)

        # Refresh (Method - 1)
        driver.refresh()

        # Refresh (Method - 2)
        driver.get(driver.current_url)

        # Open Another Url
        driver.get('https://github.com/themrinalsinha')

        # Go one step back in browser
        driver.back()

        # Going forward
        driver.forward()

        print('Getting Page Source...')
        source = driver.page_source

        # Closing the browser
        driver.close()
        driver.quit()

xx = BrowserInteractions()
xx.test()