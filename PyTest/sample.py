from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element("id", "user-name").send_keys("standard_user")

