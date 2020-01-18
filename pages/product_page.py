from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class ProductPage(BasePage): 
    def add_in_basket_page(self):
        link = self.browser.browser.find_element_by_class_name("btn btn-lg btn-primary btn-add-to-basket")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
            