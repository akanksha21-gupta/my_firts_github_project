from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# ----------------------------
# Setup WebDriver
# ----------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# ----------------------------
# Open File Upload Page
# ----------------------------
driver.get("https://the-internet.herokuapp.com/upload")

wait = WebDriverWait(driver, 10)

# ----------------------------
# Path of file to upload
# ----------------------------
file_path = os.path.abspath("sample_file.txt")

# Create a sample file if it doesn't exist
with open("sample_file.txt", "w") as f:
    f.write("This is a test file for Selenium upload.")

# ----------------------------
# Locate file input & upload file
# ----------------------------
file_input = wait.until(
    EC.presence_of_element_located((By.ID, "file-upload"))
)
file_input.send_keys(file_path)

# ----------------------------
# Click Upload button
# ----------------------------
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

# ----------------------------
# Verify success message / uploaded file name
# ----------------------------
uploaded_file = wait.until(
    EC.visibility_of_element_located((By.ID, "uploaded-files"))
)

assert "sample_file.txt" in uploaded_file.text
print("✅ File uploaded successfully!")

# ----------------------------
# Cleanup
# ----------------------------
time.sleep(2)
driver.quit()
