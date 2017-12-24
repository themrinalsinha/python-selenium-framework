from selenium import webdriver

class Automator(object):
    def __init__(self, browser='chromium'):
        self.browser = browser
        self.driver  = None

    def start(self):
        chrome_browser = '/usr/bin/chromium-browser'
        chrome_driver  = '/usr/local/bin/chromedriver'
        if self.browser is 'chromium':
            options = webdriver.ChromeOptions()
            options.binary_location = chrome_browser

        self.driver = webdriver.Chrome(executable_path = chrome_driver, chrome_options = options)

    def open(self, url):
        self.start()
        self.driver.get(url)