import re
import os
import pytest

from playwright.sync_api import Page
from pages.practiceauto.playwright.landing_page_play import LandingPagePlay

class TestFormsPagePlay:
    @pytest.mark.functional
    @pytest.mark.parametrize("message_test", ["123456789", "∀∁∂∃∄∅∆∇∈∉", "<script>alert('test');</script>"])
    def test_forms_message(self, page: Page, message_test, log_test_name):
        """
        Test that "Message received!" alert dialog appears after clicking the Submit button
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        forms_page = landing_page.click_on_forms()
        dialog_message = None

        # dialog handler
        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            dialog.accept()

        page.on("dialog", handle_dialog)
        
        # actions
        forms_page.fill_name("Karla")
        forms_page.fill_password("P@ssw0rd")
        forms_page.check_drink_2()
        forms_page.check_drink_3()
        forms_page.check_color_3()
        forms_page.select_automation_option("yes")
        forms_page.fill_email("karla@gmail.com")
        forms_page.enter_message(f"{message_test}")
        forms_page.click_submit()

        # assertions
        assert dialog_message == "Message received!"
