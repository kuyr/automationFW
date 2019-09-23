import unittest
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://10.0.6.11:9001")

elem1 = driver.find_element_by_xpath("//input[@placeholder='Access code']")
elem1.send_keys("205154202")

elem2 = driver.find_element_by_xpath("//input[@placeholder='Username']")
elem2.send_keys("olusolab")

elem3 = driver.find_element_by_xpath("//input[@id='mysecretpassword']")
elem3.send_keys("pass123*")

elem4 = driver.find_element_by_xpath("//button[@class='mybtn btn-full w-100 f-montserrat f-14']")
elem4.click()

assert "Dashboard" in driver.page_source

