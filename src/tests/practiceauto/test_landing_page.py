import logging
import pytest

from selenium import webdriver
from pages.practiceauto.selenium.landing_page import LandingPage
from utils.logger import get_logger

logger = get_logger(__name__)

class TestPracticeAutoLandingPage:
    @pytest.mark.smoke
    def test_practiceauto_landing_page(self, driver, env):
        """
        Test that the Practice Automation landing page is displayed with all options
        """
        logger.info("Environment: %s", env)

        # create the page object
        landing_page = LandingPage(driver, env)

        # verify the options displayed
        logger.info("Verifying the options displayed")
        logger.info("Delays option: " + landing_page.get_delays_option().text)
        logger.info("Forms option: " + landing_page.get_forms_option().text)
        logger.info("Popups option: " + landing_page.get_popups_option().text)
        logger.info("Sliders option: " + landing_page.get_sliders_option().text)
        logger.info("Calendars option: " + landing_page.get_calendars_option().text)
        logger.info("Modals option: " + landing_page.get_modals_option().text)
        logger.info("Tables option: " + landing_page.get_tables_option().text)
        logger.info("Window option: " + landing_page.get_window_option().text)
        logger.info("Hover option: " + landing_page.get_hover_option().text)
        logger.info("Ads option: " + landing_page.get_ads_option().text)
        logger.info("Gestures option: " + landing_page.get_gestures_option().text)
        logger.info("Download option: " + landing_page.get_download_option().text)
        logger.info("Click option: " + landing_page.get_click_option().text)
        logger.info("Spinners option: " + landing_page.get_spinners_option().text)
        logger.info("Upload option: " + landing_page.get_upload_option().text)
        logger.info("Iframes option: " + landing_page.get_iframes_option().text)
        logger.info("Images option: " + landing_page.get_images_option().text)
        logger.info("Links option: " + landing_page.get_links_option().text)
        logger.info("Accordions option: " + landing_page.get_accordions_option().text)
        assert landing_page.get_delays_option().text == "JavaScript Delays", "Delays option is not displayed"
        assert landing_page.get_forms_option().text == "Form Fields", "Forms option is not displayed"
        assert landing_page.get_popups_option().text == "Popups", "Popups option is not displayed"
        assert landing_page.get_sliders_option().text == "Sliders", "Sliders option is not displayed"
        assert landing_page.get_calendars_option().text == "Calendars", "Calendars option is not displayed"
        assert landing_page.get_modals_option().text == "Modals", "Modals option is not displayed"
        assert landing_page.get_tables_option().text == "Tables", "Tables option is not displayed"
        assert landing_page.get_window_option().text == "Window Operations", "Window Operations option is not displayed"
        assert landing_page.get_hover_option().text == "Hover", "Hover option is not displayed"
        assert landing_page.get_ads_option().text == "Ads", "Ads option is not displayed"
        assert landing_page.get_gestures_option().text == "Gestures", "Gestures option is not displayed"
        assert landing_page.get_download_option().text == "File Download", "File Download option is not displayed"
        assert landing_page.get_click_option().text == "Click Events", "Click Events option is not displayed"
        assert landing_page.get_spinners_option().text == "Spinners", "Spinners option is not displayed"
        assert landing_page.get_upload_option().text == "File Upload", "File Upload option is not displayed"
        assert landing_page.get_iframes_option().text == "Iframes", "Iframes option is not displayed"
        assert landing_page.get_images_option().text == "Broken Images", "Broken Images option is not displayed"
        assert landing_page.get_links_option().text == "Broken Links", "Broken Links option is not displayed"
        assert landing_page.get_accordions_option().text == "Accordions", "Accordions option is not displayed"
