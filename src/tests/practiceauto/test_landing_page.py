import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.practiceauto.landing_page import LandingPage

class TestPracticeAutoLandingPage:
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)

    def test_practiceauto_show_delays_page(self):
        """
        Test that the Practice Automation landing page is displayed
        """
        # navigate to the page
        self.driver.get("https://practice-automation.com/")

        landing_page = LandingPage(self.driver)
        landing_page.click_delays_option()

        # start_button = self.driver.find_element(By.ID, "start")
        # start_button.click()

        # self.wait.until(EC.text_to_be_present_in_element((By.ID, "delay"), "Liftoff!"))
        # delay_text = self.driver.find_element(By.ID, "delay")
        # assert delay_text.text == "Liftoff!"

        time.sleep(5)

    @classmethod
    def teardown_class(self):
        # Close the browser
        self.driver.quit()