from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")

dropdown = Select(driver.find_element(By.ID, "multi-select"))

dropdown.select_by_visible_text("California")
dropdown.select_by_visible_text("New York")

for option in dropdown.all_selected_options:
    print(option.text)

dropdown.deselect_by_visible_text("New York")
driver.quit()