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
    def test_delays_page_start_button(self, driver, env):
        """
        Test that "Liftoff!" text appear after clicking the Start button
        """
        # create the page object
        landing_page = LandingPage(driver, env)
        wait = WebDriverWait(driver, 15)

        # click on the delays option
        delays_page = landing_page.click_delays_option()

        delays_page.click_start_button()
        wait.until(EC.text_to_be_present_in_element(delays_page.delays_text, "Liftoff!"))

        assert delays_page.get_delay_text().text == "Liftoff!", "Text is not correct"
