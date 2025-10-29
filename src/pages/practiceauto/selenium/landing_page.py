import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.practiceauto.selenium.base_page import BasePage
from pages.practiceauto.selenium.delays_page import DelaysPage
from pages.practiceauto.selenium.click_events_page import ClickEventsPage
from config.config import BASE_URL

logger = get_logger(__name__)

class LandingPage(BasePage):
    # locators
    delays_option = (By.LINK_TEXT, "JavaScript Delays")
    forms_option = (By.LINK_TEXT, "Form Fields")
    popups_option = (By.LINK_TEXT, "Popups")
    sliders_option = (By.LINK_TEXT, "Sliders")
    calendars_option = (By.LINK_TEXT, "Calendars")
    modals_option = (By.LINK_TEXT, "Modals")
    tables_option = (By.LINK_TEXT, "Tables")
    window_option = (By.LINK_TEXT, "Window Operations")
    hover_option = (By.LINK_TEXT, "Hover")
    ads_option = (By.LINK_TEXT, "Ads")
    gestures_option = (By.LINK_TEXT, "Gestures")
    download_option = (By.LINK_TEXT, "File Download")
    click_option = (By.LINK_TEXT, "Click Events")
    spinners_option = (By.LINK_TEXT, "Spinners")
    upload_option = (By.LINK_TEXT, "File Upload")
    iframes_option = (By.LINK_TEXT, "Iframes")
    images_option = (By.LINK_TEXT, "Broken Images")
    links_option = (By.LINK_TEXT, "Broken Links")
    accordions_option = (By.LINK_TEXT, "Accordions")
    
    def __init__(self, driver, environment):
        super().__init__(driver)
        self.url = BASE_URL[environment]
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

    def click_delays_option(self):
        self.click_element(self.delays_option)
        return DelaysPage(self.driver)

    def get_delays_option(self):
        return self.find_element(self.delays_option)

    def click_forms_option(self):
        self.click_element(self.forms_option)

    def get_forms_option(self):
        return self.find_element(self.forms_option)
    
    def click_popups_option(self):
        self.click_element(self.popups_option)

    def get_popups_option(self):
        return self.find_element(self.popups_option)
    
    def click_sliders_option(self):
        self.click_element(self.sliders_option)

    def get_sliders_option(self):
        return self.find_element(self.sliders_option)
    
    def click_calendars_option(self):
        self.click_element(self.calendars_option)

    def get_calendars_option(self):
        return self.find_element(self.calendars_option)
    
    def click_modals_option(self):
        self.click_element(self.modals_option)

    def get_modals_option(self):
        return self.find_element(self.modals_option)
    
    def click_tables_option(self):
        self.click_element(self.tables_option)

    def get_tables_option(self):
        return self.find_element(self.tables_option)
    
    def click_window_option(self):
        self.click_element(self.window_option)

    def get_window_option(self):
        return self.find_element(self.window_option)
    
    def click_hover_option(self):
        self.click_element(self.hover_option)

    def get_hover_option(self):
        return self.find_element(self.hover_option)
    
    def click_ads_option(self):
        self.click_element(self.ads_option)

    def get_ads_option(self):
        return self.find_element(self.ads_option)
    
    def click_gestures_option(self):
        self.click_element(self.gestures_option)

    def get_gestures_option(self):
        return self.find_element(self.gestures_option)
    
    def click_download_option(self):
        self.click_element(self.download_option)

    def get_download_option(self):
        return self.find_element(self.download_option)
    
    def click_click_option(self):
        self.click_element(self.click_option)
        return ClickEventsPage(self.driver)

    def get_click_option(self):
        return self.find_element(self.click_option)
    
    def click_spinners_option(self):
        self.click_element(self.spinners_option)

    def get_spinners_option(self):
        return self.find_element(self.spinners_option)
    
    def click_upload_option(self):
        self.click_element(self.upload_option)

    def get_upload_option(self):
        return self.find_element(self.upload_option)
    
    def click_iframes_option(self):
        self.click_element(self.iframes_option)

    def get_iframes_option(self):
        return self.find_element(self.iframes_option)
    
    def click_images_option(self):
        self.click_element(self.images_option)

    def get_images_option(self):
        return self.find_element(self.images_option)
    
    def click_links_option(self):
        self.click_element(self.links_option)

    def get_links_option(self):
        return self.find_element(self.links_option)
    
    def click_accordions_option(self):
        self.click_element(self.accordions_option)

    def get_accordions_option(self):
        return self.find_element(self.accordions_option)
    