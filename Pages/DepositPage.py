import datetime
from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
from Pages.WithdrawlPage import Withdrawl


class DepositPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyDeposit(self):
        self.do_click(Locators.DEPOSIT_BTN)
        self.do_send_keys(Locators.ADD_AMOUNT, TestData.DEPOSITING_AMOUNT)
        # time.sleep(5)
        print(TestData.DEPOSITING_AMOUNT)
        self.do_click(Locators.AFTER_ADDING_AMOUNT_BTN)
        # time.sleep(5)
        capturingMsg = self.get_element_text(Locators.DEPOSIT_SUCCESSFULL_MSG)
        print(capturingMsg)
        assert capturingMsg == TestData.SUCCESSFULLY_DEPOSIT_AMT_MSG
        currentDate = datetime.datetime.now()
        print(currentDate.strftime("%B %d, %Y %H:%M:%S %p"))
        return Withdrawl(self.driver)
