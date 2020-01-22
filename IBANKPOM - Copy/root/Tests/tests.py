#import os
import time
import unittest
#import HtmlTestRunner
#from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from root.Pages.login_page import LoginPage
from root.Pages.dashboard_page import DashBoardPage
from root.Pages.account_page import AccountPage


class TestSuite(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        # cls.driver.maximize_window()
        cls.driver.get('http://10.0.6.11:8080/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
    #     # dir = os.getcwd()
    #     # output = open(dir +"\")

    def test_01_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("205132266")
        login.enter_password()
        login.click_login_btn()
        print('login successfully')

    def test_02_dashboard(self):
        driver = self.driver
        dashboard = DashBoardPage(driver)
        self.driver.implicitly_wait(5)
        # self.assertIn("Dashboard", self.driver.title)
        # self.assertEqual("Frequent Transaction", self.driver.page_source)
        # self.assertIn("Frequent Transfers", self.driver.page_source)
        # self.assertIn("Frequent Topup", self.driver.page_source)
        # self.assertIn("Frequent Bills", self.driver.page_source)
        # self.assertIn("GT TrackIt", self.driver.page_source)
        #dashboard.view_statement_check()
        time.sleep(5)
        # self.assertIn("View Statement", self.driver.title)
        # self.assertIn("Account Statement", driver.page_source)

        print('Dashboard Check successful')

    def test_03_accounts(self):
        driver = self.driver
        account = AccountPage(driver)
        account.driver.implicitly_wait(30)
        account.click_send_to_3rd_party()
        account.enter_country_name("Austria")
        account.select_statement("Ayegbusi")
        account.select_start_and_end_date()
        account.enter_account_to_debit("Ayegbusi")
        account.enter_role("Applicant")
        account.enter_applicant("Automated Test")
        account.click_ok()
        account.enter_token("123456")

        account.click_open_dom_account("USD")
        account.open_dom_account("test")


if __name__ == "__main__":
    unittest.main()
