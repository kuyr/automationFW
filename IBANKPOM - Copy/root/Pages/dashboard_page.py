from root.Locators.locators import LocatorsC


class DashBoardPage():
    def __init__(self, driver):
        self.driver = driver

        self.frequent_transaction_text = LocatorsC.frequent_transaction_xpath
        self.frequent_transfers_text = LocatorsC.frequent_transfers_xpath
        self.frequent_topup_text = LocatorsC.frequent_topup_xpath
        self.frequent_bills_text = LocatorsC.frequent_bills_xpath
        self.gt_track_it_text = LocatorsC.gt_track_it_xpath
        self.view_statement_btn = LocatorsC.view_statement_btn_xpath
        self.account_statement_text = LocatorsC.account_statement_xpath

    def view_statement_check(self):
        self.driver.find_element_by_xpath(self.view_statement_btn).click()




