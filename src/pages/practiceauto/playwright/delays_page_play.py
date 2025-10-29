from playwright.sync_api import Page, Locator
from pages.practiceauto.playwright.base_page_play import BasePagePlay

class DelaysPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.start_button : Locator = page.get_by_role("button", name="Start")
        self.delays_text : Locator = page.get_by_text("Liftoff!", exact=True)

    def navigate(self):
        self.navigate_url("https://practice-automation.com/javascript-delays/")

    def click_on_start_button(self):
        # actions
        self.click_element(self.start_button)
