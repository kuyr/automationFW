from MenasRoot.Locators.locators import LocatorsC


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = LocatorsC.username_textbox_xpath
        self.password_btn0 = LocatorsC.pass_btn_0_xpath
        self.password_btn1 = LocatorsC.pass_btn_1_xpath
        self.password_btn2 = LocatorsC.pass_btn_2_xpath
        self.password_btn3 = LocatorsC.pass_btn_3_xpath
        self.password_btn4 = LocatorsC.pass_btn_4_xpath
        self.password_btn5 = LocatorsC.pass_btn_5_xpath
        self.password_btn6 = LocatorsC.pass_btn_6_xpath
        self.password_btn7 = LocatorsC.pass_btn_7_xpath
        self.password_btn8 = LocatorsC.pass_btn_8_xpath
        self.password_btn9 = LocatorsC.pass_btn_9_xpath
        self.login_btn = LocatorsC.sign_in_btn_xpath
        self.proceed_btn = LocatorsC.proceed_btn_xpath

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(username)

    def enter_password(self):
        self.driver.find_element_by_xpath(self.password_btn1).click()
        self.driver.find_element_by_xpath(self.password_btn2).click()
        self.driver.find_element_by_xpath(self.password_btn3).click()
        self.driver.find_element_by_xpath(self.password_btn4).click()
        self.driver.find_element_by_xpath(self.password_btn5).click()
        self.driver.find_element_by_xpath(self.password_btn6).click()
        # self.driver.find_element_by_xpath(self.password_btn7).click()
        # self.driver.find_element_by_xpath(self.password_btn8).click()
        # self.driver.find_element_by_xpath(self.password_btn9).click()
        # self.driver.find_element_by_xpath(self.password_btn0).click()

    def click_login_btn(self):
        self.driver.find_element_by_xpath(self.login_btn).click()
        self.driver.find_element_by_xpath(self.proceed_btn).click()

