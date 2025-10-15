import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.practiceauto.selenium.base_page import BasePage

logger = get_logger(__name__)

class DelaysPage(BasePage):
    # locators
    start_button = (By.ID, "start")
    delays_text = (By.ID, "delay")

    def __init__(self, driver):
        super().__init__(driver)

    def click_start_button(self):
        self.click_element(self.start_button)

    def get_start_button(self):
        return self.find_element(self.start_button)
    
    def get_delay_text(self):
        return self.find_element(self.delays_text)