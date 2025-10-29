import logging
import pytest

from selenium import webdriver
from pages.practiceauto.selenium.landing_page import LandingPage
from utils.logger import get_logger

logger = get_logger(__name__)

class TestPracticeAutoClickEventsPage:
    @pytest.mark.functional
    @pytest.mark.smoke
    def test_demo_text(self, driver, env, log_test_name):
        """
        Test that the expected text is present on the screen based on the clicked button
        """
        # create the page object
        landing_page = LandingPage(driver, env)

        # click on the click events option
        landing_page.scroll_to_element(landing_page.ads_option)
        click_events_page = landing_page.click_click_option()

        # actions and assertions
        click_events_page.click_cat_button()
        assert click_events_page.get_demo_text().text == "Meow!", "Text is not correct"

        click_events_page.click_dog_button()
        assert click_events_page.get_demo_text().text == "Woof!", "Text is not correct"

        click_events_page.click_pig_button()
        assert click_events_page.get_demo_text().text == "Oink!", "Text is not correct"

        click_events_page.click_cow_button()
        assert click_events_page.get_demo_text().text == "Moo!", "Text is not correct"

    @pytest.mark.parametrize("button, demo_text", [("cat", "Meow!"), ("dog", "Woof!"), ("pig", "Oink!"), ("cow", "Moo!")])
    def test_demo_text2(self, driver, env, button, demo_text, log_test_name):
        """
        Test that the expected text is present on the screen based on the clicked button
        """
        # create the page object
        landing_page = LandingPage(driver, env)

        # click on the click events option
        landing_page.scroll_to_element(landing_page.ads_option)
        click_events_page = landing_page.click_click_option()

        # actions
        click_events_page.click_event_button(button)
        expected_text = click_events_page.get_demo_text().text

        # asserts
        assert expected_text == demo_text, "Text is not correct"

    @pytest.mark.parametrize("read_data", ["buttons"], indirect=True)
    def test_demo_text3(self, driver, env, read_data, log_test_name):
        """
        Test that the expected text is present on the screen based on the clicked button
        """
        # create the page object
        landing_page = LandingPage(driver, env)

        # click on the click events option
        landing_page.scroll_to_element(landing_page.ads_option)
        click_events_page = landing_page.click_click_option()

        # actions
        for data in read_data:
            click_events_page.click_event_button(data["button"])
            expected_text = click_events_page.get_demo_text().text

        # asserts
        assert expected_text == data['demo_text'], "Text is not correct"
