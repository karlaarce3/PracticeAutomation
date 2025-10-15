from playwright.sync_api import Page, Locator
from pages.practiceauto.playwright.base_page_play import BasePagePlay

class FormsPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.name : Locator = page.get_by_test_id("name-input")
        self.password : Locator = page.get_by_role("textbox", name="Password")
        self.drink_2 : Locator = page.get_by_test_id("drink2")
        self.drink_3 : Locator = page.get_by_test_id("drink3")
        self.color_3 : Locator = page.get_by_test_id("color3")
        self.automation : Locator = page.get_by_test_id("automation")
        self.email : Locator = page.get_by_test_id("email")
        self.message : Locator = page.get_by_test_id("message")
        self.submit : Locator = page.get_by_test_id("submit-btn")

    def navigate(self):
        self.navigate_url("https://practice-automation.com/form-fields/")

    def fill_name(self, name):
        # actions
        self.enter_text(self.name, name)

    def fill_password(self, password):
        # actions
        self.enter_text(self.password, password)
    
    def check_drink_2(self):
        # actions
        self.check_checkbox(self.drink_2)

    def check_drink_3(self):
        # actions
        self.check_checkbox(self.drink_3)

    def check_color_3(self):
        # actions
        self.check_checkbox(self.color_3)

    def select_automation_option(self, option):
        # actions
        self.choose_option(self.automation, option)

    def fill_email(self, email):
        # actions
        self.enter_text(self.email, email)

    def enter_message(self, message):
        # actions
        self.enter_text(self.message, message)

    def click_submit(self):
        # actions
        self.click_element(self.submit)
