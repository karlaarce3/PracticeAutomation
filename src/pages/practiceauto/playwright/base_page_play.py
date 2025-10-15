from playwright.sync_api import Page, Locator
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePagePlay():
    def __init__(self, page: Page):
        self.page = page

    def navigate_url(self, url):
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def click_element(self, locator):
        '''Click on element'''
        tag_name, element_name = self.get_tag_and_text(locator)
        logger.info(f"Clicking on {element_name} element: {tag_name}")
        locator.click()

    def focus_element(self, locator):
        '''Focus on element'''
        tag_name, element_name = self.get_tag_and_text(locator)
        logger.info(f"Focusing on {element_name} element: {tag_name}")
        locator.focus()

    def enter_text(self, locator, text):
        """Enter text into input field"""      
        tag_name, element_name = self.get_tag_and_text(locator)  
        logger.info(f"Entering text '{text}' into {element_name} element: {tag_name}")
        locator.fill(text)

    def check_checkbox(self, locator):
        """Checking option"""      
        tag_name, element_name = self.get_tag_and_text(locator)  
        logger.info(f"Checking {element_name} element: {tag_name}")
        locator.check()

    def choose_option(self, locator, option):
        """Selecting an option from dropdown"""      
        tag_name, element_name = self.get_tag_and_text(locator)  
        logger.info(f"Selecting '{option}' from {element_name} element: {tag_name}")
        locator.select_option(option)

    def get_tag_and_text(self, locator):
        '''Get tag name and text from locator'''
        # get tag from locator
        tag_name = locator.evaluate("node => node.tagName")

        # get text from locator
        if locator.inner_text():
            element_name = locator.inner_text()
        else:
            element_name = tag_name
        return tag_name, element_name
