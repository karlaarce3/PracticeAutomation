from playwright.sync_api import Page, Locator
from pages.practiceauto.playwright.base_page_play import BasePagePlay
from pages.practiceauto.playwright.delays_page_play import DelaysPagePlay
from pages.practiceauto.playwright.forms_page_play import FormsPagePlay

class LandingPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.delays : Locator = page.get_by_role("link", name="JavaScript Delays")
        self.forms : Locator = page.get_by_role("link", name="Form Fields")
        self.popups : Locator = page.get_by_role("link", name="Popups")
        self.sliders : Locator = page.get_by_role("link", name="Sliders")
        self.calendars : Locator = page.get_by_role("link", name="Calendars")
        self.modals : Locator = page.get_by_role("link", name="Modals")
        self.tables : Locator = page.get_by_role("link", name="Tables")
        self.windows : Locator = page.get_by_role("link", name="Window Operations")
        self.hover : Locator = page.get_by_role("link", name="Hover")
        self.ads : Locator = page.get_by_role("link", name="Ads")
        self.gestures : Locator = page.get_by_role("link", name="Gestures")
        self.download : Locator = page.get_by_role("link", name="File Download")
        self.click : Locator = page.get_by_role("link", name="Click Events")
        self.spinners : Locator = page.get_by_role("link", name="Spinners")
        self.upload : Locator = page.get_by_role("link", name="File Upload")
        self.iframes : Locator = page.get_by_role("link", name="Iframes")
        self.images : Locator = page.get_by_role("link", name="Broken Images")
        self.links : Locator = page.get_by_role("link", name="Broken Links")
        self.accordions : Locator = page.get_by_role("link", name="Accordions")

    def navigate(self):
        self.navigate_url(url="https://practice-automation.com/")
    
    def click_on_delays(self):
        self.click_element(self.delays)
        return DelaysPagePlay(self.page)
    
    def click_on_forms(self):
        self.click_element(self.forms)
        return FormsPagePlay(self.page)
    
    def click_on_popups(self):
        self.click_element(self.popups)

    def click_on_sliders(self):
        self.click_element(self.sliders)

    def click_on_calendars(self):
        self.click_element(self.calendars)

    def click_on_modals(self):
        self.click_element(self.modals)

    def click_on_tables(self):
        self.click_element(self.tables)

    def click_on_windows(self):
        self.click_element(self.windows)

    def click_on_hover(self):
        self.click_element(self.hover)

    def click_on_ads(self):
        self.click_element(self.ads)

    def click_on_gestures(self):
        self.click_element(self.gestures)

    def click_on_download(self):
        self.click_element(self.download)

    def click_on_click(self):
        self.click_element(self.click)

    def click_on_spinners(self):
        self.click_element(self.spinners)

    def click_on_upload(self):
        self.click_element(self.upload)

    def click_on_iframes(self):
        self.click_element(self.iframes)

    def click_on_images(self):
        self.click_element(self.images)

    def click_on_links(self):
        self.click_element(self.links)

    def click_on_accordions(self):
        self.click_element(self.accordions)
