import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class ManagerLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def managerLoginOption(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        addCust = self.get_element_text(Locators.ADD_CUSTOMERS)
        print('\nTitle :', addCust)
        assert addCust == "Add Customer"
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def verifyingTitle(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        title = self.get_title()
        print('\nTitle :', title)
        assert title == "XYZ Bank"
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
