# ADVANCE LOCATORS
from selenium import webdriver

class AdvanceLocator(object):
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver  = webdriver.Chrome()
        driver.get(baseUrl)

        # # Advanced Locator
        # CSS Locator : input[id="displayed-text"]
        # CSS Locator : input#displayed-text
        #  use '#' for id and '.' for class

        # .inputs -> it will git all the class with this name
        # input.inputs#name -> input tag with class inputs and id name

        # Using wild card with CSS selector
        # '^' -> Represents the starting text
        # '$' -> Represents the ending text
        # '*' -> Represents the text contained
        # eg : input[class^='inputs'] # this will return 2 match one is exact match and all where class starts with inputs
        # eg : input[class$='displayed-class'] # this will retun all the class which ends with displayed-text
        # eg : input[placeholder*='Enter'] # this will return anywhere where Enter appear in placeholder

        # # Finding Children
        # eg: fieldset>table
        # eg: filedset>#product | fieldset tag then id product

# find element
ff = AdvanceLocator()
ff.test()