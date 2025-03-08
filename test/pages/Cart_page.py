from selenium import webdriver
from selenium.webdriver.common.by import By

from lib.reporter import Reporter
from lib.selenium_extensions import (Click, findElementBy, isDisplayed,
                                     isEnabled, isSelected, sendKeys,
                                     waitUntilDisplay, waitUntilExistInDOM,
                                     waitUntilHidden)


class Cart_page:
    
    driver = None

    def __init__(self,driver):
        self.driver = driver

        