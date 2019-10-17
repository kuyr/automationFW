from root.Locators.locators import LocatorsC


class AccountModulePage():
    def __init__(self, driver):
        self.driver = driver

        self.send_to_3rd_party_btn = LocatorsC.Send_state_to_3rd_party_xpath
        self.open_dorm_acct_btn = LocatorsC.open_dom_acct_xpath
        self.open_additional_acct_btn = LocatorsC.open_additional_act_xpath

    def send_to_3rd_party_check(self):
        self.driver.find_element_by_xpath(self.send_to_3rd_party_btn).click()

    def open_dorm_acct_check(self):
        self.driver.find_element_by_xpath(self.open_dorm_acct_btn).click()

    def open_additional_acct_check(self):
        self.driver.find_element_by_xpath(self.open_additional_acct_btn).click()
