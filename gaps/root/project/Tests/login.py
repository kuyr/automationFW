import os
import sys
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from project.Pages.homePage import HomePage
from project.Pages.loginPage import LoginPage
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class AllTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        driver = self.driver
        driver.get("http://10.0.6.11:9001")
        login = LoginPage(driver)

        login.enter_accesscode("205154202")
        login.enter_username("olusolab")
        login.enter_password("pass123*")
        login.click_login()

        assert "Dashboard" in driver.page_source

        time.sleep(2)
        # self.assertEqual(True, False)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/appdevmacbook2/PycharmProjects/SeleniumPom'
                                                                  '/project/Reports'))
