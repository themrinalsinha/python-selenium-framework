from selenium import webdriver
from .        import terminal_output

class Automator(object):
    def __init__(self, browser='chromium'):
        self.browser = browser
        self.driver  = None

    def start(self):
        self.stop()
        options = webdriver.ChromeOptions()
        options.binary_location = terminal_output('which chromium-browser')
        chrome_driver = terminal_output('which chromedriver')
        self.driver   = webdriver.Chrome(executable_path = chrome_driver, 
                                         chrome_options  = options)
        self.handle   = self.driver.current_window_handle
        return self

    def stop(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
            self.handle = None

    def open(self, url):
        self.start()
        self.driver.get(url)
