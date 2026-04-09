from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------------------------------
# 1. Start the browser
# -------------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------
# 2. Open demo page
# -------------------------------
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# -------------------------------
# 3. Click Start button
# -------------------------------
start_button = driver.find_element(By.TAG_NAME, "button")
start_button.click()

# -------------------------------
# 4. Explicit Wait
# -------------------------------
# Wait up to 10 seconds for the text "Hello World!" to become visible
wait = WebDriverWait(driver, 10)

hello_text = wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

# -------------------------------
# 5. Print the result
# -------------------------------
print("Loaded text is:", hello_text.text)

# -------------------------------
# 6. Close browser
# -------------------------------
time.sleep(2)
driver.quit()