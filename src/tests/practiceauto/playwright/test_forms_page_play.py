import re
import os

from config.config import user_name, password, mail
from playwright.sync_api import Page, expect
from pages.practiceauto.playwright.landing_page_play import LandingPagePlay

class TestFormsPagePlay:
    def test_forms(self, page: Page):
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        forms_page = landing_page.click_on_forms()
        
        forms_page.fill_name(user_name)
        forms_page.fill_password(password)
        forms_page.check_drink_2()
        forms_page.check_drink_3()
        forms_page.check_color_3()
        forms_page.select_automation_option("yes")
        forms_page.fill_email(mail)
        forms_page.enter_message("Hello")
        forms_page.click_submit()
        page.once("dialog", lambda dialog: dialog.dismiss())
