import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.practiceauto.selenium.base_page import BasePage

logger = get_logger(__name__)

class ClickEventsPage(BasePage):
    # locators
    cat_button = (By.XPATH, "//button[@onclick='catSound()']")
    dog_button = (By.XPATH, "//button[@onclick='dogSound()']")
    pig_button = (By.XPATH, "//button[@onclick='pigSound()']")
    cow_button = (By.XPATH, "//button[@onclick='cowSound()']")
    demo_text = (By.ID, "demo")

    buttons_locators = {
        "cat": cat_button,
        "dog": dog_button,
        "pig": pig_button,
        "cow": cow_button
    }

    def __init__(self, driver):
        super().__init__(driver)

    def click_cat_button(self):
        self.click_element(self.cat_button)

    def get_cat_button(self):
        return self.find_element(self.cat_button)
    
    def click_dog_button(self):
        self.click_element(self.dog_button)

    def get_dog_button(self):
        return self.find_element(self.dog_button)
    
    def click_pig_button(self):
        self.click_element(self.pig_button)

    def get_pig_button(self):
        return self.find_element(self.pig_button)
    
    def click_cow_button(self):
        self.click_element(self.cow_button)

    def get_cow_button(self):
        return self.find_element(self.cow_button)
    
    def get_demo_text(self):
        return self.find_element(self.demo_text)
    
    def click_event_button(self, button):
        self.click_element(self.buttons_locators[button])
