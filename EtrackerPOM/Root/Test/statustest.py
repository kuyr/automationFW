import unittest
import time

# from webbrowser import get

from selenium import webdriver
from Root.Pages.etrackertest import EtrackerStatus


class EtrackerTestCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/oghenetega.ekakitie/Desktop/chromedriver")
        cls.driver.get("http://10.0.6.11:8086")
        cls.driver.implicitly_wait(9)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_status(self):
        driver = self.driver
        status = EtrackerStatus(driver)
        status.card_type()
        time.sleep(3)
        #status.regular_opt()
        #time.sleep(3)
        status.select_action()
        #time.sleep(3)
        #status.collect_opt()
        time.sleep(3)
        status.nuban("0120708490")
        time.sleep(5)
        status.click_it()
        time.sleep(3)
        #assert "0915" in driver.current_window_handle
        status.view_it()
        time.sleep(3)
        #status.own_opt()
        #time.sleep(3)
        #status.submit_btn()

        time.sleep(5)

        #assert "LastLoginDate" in driver.current_window_handle
        #print("Launch Successfully")


if __name__ == '__main__':
    unittest.main()
