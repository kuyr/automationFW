from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://mail.yahoo.com")

driver.find_element_by_xpath("//input[@id='login-username']").send_keys("femlabond@yahoo.com")
driver.find_element_by_xpath("//input[@id='login-signin']").click()
driver.find_element_by_xpath("//input[@id='login-passwd']").send_keys("******")
driver.find_element_by_xpath("//button[@id='login-signin']").click()

driver.quit()