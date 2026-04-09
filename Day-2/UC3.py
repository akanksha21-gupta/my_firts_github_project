from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# -----------------------------
# Start browser
# -----------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# Replace with your page URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)

# -----------------------------
# Locate the dropdown
# -----------------------------
dropdown_element = driver.find_element(By.ID, "dropdown-class-example")

# Create Select object
dropdown = Select(dropdown_element)

# -----------------------------
# Verify dropdown is multi-select
# -----------------------------
if not dropdown.is_multiple:
    print("Dropdown does not support multi-select")
    driver.quit()
    exit()

# -----------------------------
# Select multiple options
# -----------------------------
dropdown.select_by_visible_text("Option1")
dropdown.select_by_visible_text("Option2")
dropdown.select_by_visible_text("Option3")

# -----------------------------
# Print all selected options
# -----------------------------
print("Selected options:")
for option in dropdown.all_selected_options:
    print(option.text)

# -----------------------------
# Deselect one option
# -----------------------------
dropdown.deselect_by_visible_text("Option2")

print("\nAfter deselecting 'Java':")
for option in dropdown.all_selected_options:
    print(option.text)

# -----------------------------
# Optional: Deselect all
# -----------------------------
# dropdown.deselect_all()

time.sleep(2)
driver.quit()