from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --------------------------------
# Start browser
# --------------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# --------------------------------
# Open page that opens a new window
# --------------------------------
driver.get("https://the-internet.herokuapp.com/windows")

wait = WebDriverWait(driver, 10)

# --------------------------------
# Store parent window handle
# --------------------------------
parent_window = driver.current_window_handle

# --------------------------------
# Click link that opens new window
# --------------------------------
driver.find_element(By.LINK_TEXT, "Click Here").click()

# --------------------------------
# Wait until new window opens
# --------------------------------
wait.until(lambda d: len(d.window_handles) > 1)

# --------------------------------
# Switch to new window
# --------------------------------
for handle in driver.window_handles:
    if handle != parent_window:
        driver.switch_to.window(handle)
        break

# --------------------------------
# Extract heading text from new window
# --------------------------------
heading_text = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "h3"))
).text

print("Heading text from new window:", heading_text)

# --------------------------------
# Close new window and switch back
# --------------------------------
driver.close()
driver.switch_to.window(parent_window)

driver.quit()
