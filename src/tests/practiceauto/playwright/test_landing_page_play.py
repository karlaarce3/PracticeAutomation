import re
import pytest

from playwright.sync_api import Page, expect
from pages.practiceauto.playwright.landing_page_play import LandingPagePlay

class TestLandingPagePlay:
    @pytest.mark.smoke
    def test_landing_page(self, page: Page, log_test_name):
        """
        Test that the Practice Automation landing page is displayed with all options
        """
        landing_page = LandingPagePlay(page)
        landing_page.navigate()

        # assertions
        expect(landing_page.delays).to_be_visible()
        expect(landing_page.delays).to_contain_text("JavaScript Delays")
        expect(landing_page.forms).to_contain_text("Form Fields")
        expect(landing_page.popups).to_contain_text("Popups")
        expect(landing_page.sliders).to_contain_text("Sliders")
        expect(landing_page.calendars).to_contain_text("Calendars")
        expect(landing_page.modals).to_contain_text("Modals")
        expect(landing_page.tables).to_contain_text("Tables")
        expect(landing_page.windows).to_contain_text("Window Operations")
        expect(landing_page.hover).to_contain_text("Hover")
        expect(landing_page.ads).to_contain_text("Ads")
        expect(landing_page.gestures).to_contain_text("Gestures")
        expect(landing_page.download).to_contain_text("File Download")
        expect(landing_page.click).to_contain_text("Click Events")
        expect(landing_page.spinners).to_contain_text("Spinners")
        expect(landing_page.upload).to_contain_text("File Upload")
        expect(landing_page.iframes).to_contain_text("Iframes")
        expect(landing_page.images).to_contain_text("Broken Images")
        expect(landing_page.links).to_contain_text("Broken Links")
        expect(landing_page.accordions).to_contain_text("Accordions")
