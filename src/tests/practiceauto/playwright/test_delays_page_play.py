import re

from playwright.sync_api import Page, expect
from pages.practiceauto.playwright.landing_page_play import LandingPagePlay

class TestDelaysPagePlay:
    def test_delays_page(self, page: Page) -> None:
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        delays_page = landing_page.click_on_delays()

        delays_page.navigate()
        delays_page.click_on_start_button()
        delays_page.focus_on_delays_text()

        # assertions
        expect(delays_page.delays_text).to_be_visible()
        expect(delays_page.delays_text).to_contain_text("Liftoff!")
