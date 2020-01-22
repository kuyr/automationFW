from Root.Locators.locators import LocatorsE
from selenium.webdriver.support.ui import Select



class EtrackerStatus():
    def __init__(self, driver):
        self.driver = driver
        self.driver.cardtype_btn_xpath = LocatorsE.cardtype_btn_xpath
        self.driver.regular_btn_xpath = LocatorsE.regular_btn_xpath
        self.driver.action_btn_xpath = LocatorsE.action_btn_xpath
        self.driver.collection_btn_xpath = LocatorsE.collection_btn_xpath
        self.driver.AcctNum_textbox_xpath = LocatorsE.AcctNum_textbox_xpath
        #self.driver.Go_click_xpath = LocatorsE.Go_click_xpath
        self.driver.Go_click_css_selector = LocatorsE.Go_click_css_selector
        #self.driver.view_click_xpath = LocatorsE.view_click_xpath
        self.driver.view_click_css_selector = LocatorsE.view_click_css_selector
        self.driver.self_click_xpath = LocatorsE.self_click_xpath
        self.driver.self_submit_btn_xpath = LocatorsE.submit_btn_xpath

    def card_type(self):
        card_type = Select(self.driver.find_element_by_xpath(self.driver.cardtype_btn_xpath))
        card_type.select_by_visible_text("Regular")        
        regular_opt = self.driver.find_element_by_xpath(self.driver.regular_btn_xpath).click
        #select = Select(driver.find_element_by_id('rating'))
        #select.select_by_index("3")
        #// or
        #select.select_by_visible_text("It's OK")
        #// or
        #select.select_by_value("3")

    #def regular_opt(self):
        #regular_opt = self.driver.find_element_by_xpath(self.driver.regular_btn_xpath).click

    def select_action(self):
        select_action = Select(self.driver.find_element_by_xpath(self.driver.action_btn_xpath))
        select_action.select_by_visible_text("COLLECTION")        
        regular_opt = self.driver.find_element_by_xpath(self.driver.regular_btn_xpath).click

    #def collect_opt(self):
        #collect_opt = self.driver.find_element_by_xpath(self.driver.collection_btn_xpath).click

    def nuban(self, actno):
        self.driver.find_element_by_xpath(self.driver.AcctNum_textbox_xpath).send_keys(actno)

    def click_it(self):
        #click_it = self.driver.find_element_by_xpath(self.driver.Go_click_xpath).click
        click_it = self.driver.find_element_by_css_selector("#button-addon2").click()
        click_it = self.driver.find_element_by_css_selector("#button-addon2").click()
        click_it = self.driver.find_element_by_css_selector("#button-addon2").click()


    def view_it(self):
        #view_it = self.driver.find_element_by_xpath(self.driver.view_click_xpath).click
        view_it = self.driver.find_element_by_css_selector(self.driver.view_click_css_selector).click
    def own_opt(self):
        own_opt = self.driver.find_element_by_xpath(self.driver.self_click_xpath).click

    def submit_btn(self):
        submit_btn = self.driver.find_element_by_xpath(self.driver.self_submit_btn_xpath).click
