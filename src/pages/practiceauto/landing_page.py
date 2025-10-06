import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.practiceauto.base_page import BasePage

logger = get_logger(__name__)

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.delays_option = (By.LINK_TEXT, "JavaScript Delays")
        self.forms_option = (By.LINK_TEXT, "Form Fields")

    def click_delays_option(self):
        self.click_element(self.delays_option)

    def click_forms_option(self):
        self.click_element(self.forms_option)