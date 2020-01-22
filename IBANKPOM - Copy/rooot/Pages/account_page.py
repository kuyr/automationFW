import time
from selenium.webdriver.common.keys import Keys
from rooot.Locators.locators import LocatorsC


class AccountPage():
    def __init__(self, driver):
        self.driver = driver

        self.view_statement_btn = LocatorsC.view_statement_btn_xpath

        self.send_to_3rd_party_btn = LocatorsC.send_to_3rd_party_btn_xpath
        # self.open_dom_acct_btn = LocatorsC.open_dom_acct_xpath
        # self.open_additional_acct_btn = LocatorsC.open_additional_act_xpath
        self.enter_country_name_textbox = LocatorsC.enter_country_textbox_xpath
        # self.select_country_option = LocatorsC.select_country_option_xpath
        self.enter_account_statement_name = LocatorsC.enter_statement_acct_textbox_xpath
        #####
        self.select_start_date_icon_xpath = LocatorsC.select_start_date_icon_xpath
        self.select_start_date_xpath = LocatorsC.select_start_date_xpath
        self.select_end_date_icon_xpath = LocatorsC.select_end_date_icon_xpath
        self.select_end_date_xpath = LocatorsC.select_end_date_xpath
        ###
        self.enter_account_to_debit1_xpath = LocatorsC.enter_account_to_debit_xpath
        self.enter_role_xpath = LocatorsC.enter_role_xpath
        self.enter_applicant_xpath = LocatorsC.enter_applicant_xpath
        self.click_send_xpath = LocatorsC.click_send_statement_btn_xpath
        self.click_ok_xpath = LocatorsC.click_ok_bt_xpath
        self.enter_token_xpath = LocatorsC.enter_token_xpath
        self.submit_btn_xpath = LocatorsC.submit_btn_xpath
        ####
        self.click_open_dom_account = LocatorsC.open_dom_account_btn_xpath
        self.enter_currency_type_xpath = LocatorsC.enter_currency_type_xpath
        self.enter_secret_question_xpath = LocatorsC.enter_secret_question_xpath
        self.click_accept_checkbox_xpath = LocatorsC.accept_checkbox_xpath
        self.click_submit_validate_xpath = LocatorsC.submit_btn_validate_xpath
        #####
        self.click_open_additional_account_xpath = LocatorsC.open_additional_account_btn_xpath
        self.enter_account_type_xpath = LocatorsC.enter_account_type_xpath
        self.success_text_xpath = LocatorsC.success_text_xpath

    def click_send_to_3rd_party(self):
        self.driver.find_element_by_xpath(self.view_statement_btn).click()
        self.driver.find_element_by_xpath(self.send_to_3rd_party_btn).click()

    def enter_country_name(self, country):
        self.driver.find_element_by_xpath(self.enter_country_name_textbox).send_keys(country)
        # time.sleep(5)
        self.driver.find_element_by_xpath(self.enter_country_name_textbox).send_keys(Keys.RETURN)

    def select_statement(self, account_name1):
        self.driver.find_element_by_xpath(self.enter_account_statement_name).send_keys(account_name1)
        # time.sleep(5)
        self.driver.find_element_by_xpath(self.enter_account_statement_name).send_keys(Keys.RETURN)

    def select_start_and_end_date(self):
        self.driver.find_element_by_xpath(self.select_start_date_icon_xpath).click()
        self.driver.find_element_by_xpath(self.select_start_date_xpath).click()
        self.driver.find_element_by_xpath(self.select_end_date_icon_xpath).click()
        self.driver.find_element_by_xpath(self.select_end_date_xpath).click()

    def enter_account_to_debit(self, account_name2):
        self.driver.find_element_by_xpath(self.enter_account_to_debit1_xpath).send_keys(account_name2)
        # time.sleep(5)
        self.driver.find_element_by_xpath(self.enter_account_to_debit1_xpath).send_keys(Keys.RETURN)

    def enter_role(self, role):
        self.driver.find_element_by_xpath(self.enter_role_xpath).send_keys(role)
        # time.sleep(5)
        self.driver.find_element_by_xpath(self.enter_role_xpath).send_keys(Keys.RETURN)

    def enter_applicant(self, applicant):
        self.driver.find_element_by_xpath(self.enter_applicant_xpath).send_keys(applicant)
        # time.sleep(5)
        self.driver.find_element_by_xpath(self.enter_applicant_xpath).send_keys(Keys.RETURN)

    def click_ok(self):
        self.driver.find_element_by_xpath(self.click_ok_xpath).click()

    def enter_token(self, token):
        self.driver.find_element_by_xpath(self.enter_token_xpath).send_keys(token)
        # time.sleep(5)
        # self.driver.find_element_by_xpath(self.enter_token_xpath).send_keys(Keys.RETURN)
        self.driver.find_element_by_xpath(self.submit_btn_xpath).click()
        self.driver.find_element_by_xpath(self.click_open_dom_account).click()

    def click_open_dom_account(self, currency):

        self.driver.find_element_by_xpath(self.enter_currency_type_xpath).send_keys(currency)
        self.driver.find_element_by_xpath(self.enter_currency_type_xpath).send_keys(Keys.RETURN)

    def open_dom_account(self, secret):
        self.driver.find_element_by_xpath(self.enter_secret_question_xpath).send_keys(secret)
        self.driver.find_element_by_xpath(self.enter_secret_question_xpath).send_keys(Keys.RETURN)
        self.driver.find_element_by_xpath(self.click_accept_checkbox_xpath).click()
        self.driver.find_element_by_xpath(self.click_submit_validate_xpath).click()

    # def open_dom_acct_check(self):
    #     self.driver.find_element_by_xpath(self.open_dom_acct_btn).click()
    #
    # def open_additional_acct_check(self):
    #     self.driver.find_element_by_xpath(self.open_additional_acct_btn).click()
