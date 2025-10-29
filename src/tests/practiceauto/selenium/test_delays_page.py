import logging
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.practiceauto.selenium.landing_page import LandingPage
from utils.logger import get_logger

logger = get_logger(__name__)

class TestPracticeAutoDelaysPage:
    @pytest.mark.functional
    @pytest.mark.smoke
    def test_delays_page_start_button(self, driver, env, log_test_name):
        """
        Test that "Liftoff!" text appears after clicking the Start button
        """
        # create the page object
        landing_page = LandingPage(driver, env)

        # click on the delays option
        landing_page.scroll_to_element(landing_page.delays_image)
        delays_page = landing_page.click_delays_option()

        # actions
        delays_page.click_start_button()
        wait = WebDriverWait(driver, 15)
        wait.until(EC.text_to_be_present_in_element(delays_page.delays_text, "Liftoff!"))

        # asserts
        assert delays_page.get_delay_text().text == "Liftoff!", "Text is not correct"
