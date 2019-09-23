from project.Locators.locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.access_textbox_id = Locators.access_textbox_xpath
        self.username_textbox_id = Locators.username_textbox_xpath
        self.password_textbox_id = Locators.password_textbox_xpath
        self.login_button_id = Locators.login_button_xpath

    def enter_accesscode(self, accesscode):
        self.driver.find_element_by_id(self.access_textbox_id).clear()
        self.driver.find_element_by_id(Locators.access_textbox_xpath).send_keys(accesscode)

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.login_button_xpath).click()
