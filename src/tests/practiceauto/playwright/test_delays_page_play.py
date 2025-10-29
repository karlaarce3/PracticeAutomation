import re
import time
import pytest

from playwright.sync_api import Page, expect
from pages.practiceauto.playwright.landing_page_play import LandingPagePlay

class TestDelaysPagePlay:
    @pytest.mark.functional
    @pytest.mark.smoke
    def test_delays_page(self, page: Page, log_test_name):
        """
        Test that "Liftoff!" text appears after clicking the Start button
        """
        # navigate to the delays page
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        delays_page = landing_page.click_on_delays()
        delays_page.navigate()

        # actions
        delays_page.click_on_start_button()
        time.sleep(10)

        # assertions
        expect(delays_page.delays_text).to_be_visible()
        expect(delays_page.delays_text).to_contain_text("Liftoff!")
