from Pages.DepositingAmountWithRegisteredUser import DepositingAmountWithRegisteredUser
from Pages.LoginWithRegisteredUsers import LoginWithRegisteredUser
from Pages.VerifyingTransactionsWithRegisteredUser import VerifyingTransactionWithRegisteredUser
from Pages.WithdrawlAmountWithRegisteredUser import WithdrawlAmountWithRegisteredUser
from Tests.test_Base import BaseTest


class Test_VerifyingTransactionWithRegisteredUser(BaseTest):
    def test_verifyTransactionWithRegUser(self):
        registerCust = LoginWithRegisteredUser(self.driver)
        registerCust.logIn()
        depoAmount = DepositingAmountWithRegisteredUser(self.driver)
        depoAmount.verifyDepoAmountWithRegisteredUser()
        withdrewAmount = WithdrawlAmountWithRegisteredUser(self.driver)
        withdrewAmount.verifyAmountWithdrawlWithRedUsers()
        transactionVerify = VerifyingTransactionWithRegisteredUser(self.driver)
        transactionVerify.verifyTransactionsWithRegUser()
