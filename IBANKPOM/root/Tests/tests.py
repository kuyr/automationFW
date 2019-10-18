import os
import time
import unittest
#import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from root.Pages.login_page import LoginPage
from root.Pages.dashboard_page import DashBoardPage
from root.Pages.account_page import AccountPage


class TestSuite(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(20)
        # cls.driver.maximize_window()
        cls.driver.get('http://10.0.6.11:8080/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        # dir = os.getcwd()
        # output = open(dir +"\")

    def test_01_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("205132266")
        login.enter_password()
        login.click_login_btn()
        print('login successfully')





    # def test_02_dashboard(self):
    #     driver = self.driver
    #     dashboard = DashBoardPage(driver)
    #     self.driver.implicitly_wait(5)
    #     self.assertIn("Dashboard", self.driver.title)
    #     self.assertIn("Frequent Transaction", self.driver.page_source)
    #     self.assertIn("Frequent Transfers", self.driver.page_source)
    #     self.assertIn("Frequent Topup", self.driver.page_source)
    #     self.assertIn("Frequent Bills", self.driver.page_source)
    #     self.assertIn("GT TrackIt", self.driver.page_source)
    #     dashboard.view_statement_check()
    #     time.sleep(5)
    #     self.assertIn("View Statement", self.driver.title)
    #     self.assertIn("Account Statement", driver.page_source)
    #
    #     print('Dashboard Check successful')
    #
    # def test_03_accounts(self):
    #     driver = self.driver
    #     account = AccountPage(driver)
    #
    #
    #
    #
    #
    #
    #
    #     account.send_to_3rd_party_check()
    #     self.assertIn("Generate Statement", self.driver.title)
    #     account.send_to_3rd_party_check()
    #     driver.find_element_by_xpath("//span[contains(text(),'United Kingdom')]").click()
    #     driver.find_element_by_xpath("//div[@id='aa01fee5fafe-0']//p[1]").click()
    #
    #     time.sleep(5)
    #     print('Generate Statement Check successful')
    #
    # def test_04_account_open_dom_act(self):
    #     driver = self.driver
    #     account = AccountModulePage(driver)
    #     account.open_dorm_acct_check()
    #     time.sleep(5)
    #     self.assertIn("Open Dom Account", self.driver.title)
    #     print('Open Dom Account Check successful')
    #
    # def test_05_account_open_additional_act(self):
    #     driver = self.driver
    #     account = AccountModulePage(driver)
    #     account.open_additional_acct_check()
    #     time.sleep(5)
    #     self.assertIn("Add Additional Account", self.driver.title)
    #     print('Open Additional Account Successful')

if __name__ == "__main__":
    unittest.main()
