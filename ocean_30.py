from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

driver = webdriver.Chrome()
driver.get("https://ecommercewebsite.com")

# ✅ Blank 1: Initialize Fluent Wait (20 seconds, polling every 2 sec)
wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
)

# Wait for the search input to be visible and ready
search_input = wait.until(
    EC.visibility_of_element_located((By.ID, "search-input"))
)

# ✅ Blank 2: Enter product name
search_input.send_keys("Laptop")
search_input.send_keys(Keys.ENTER)

# Wait for the color filter dropdown to be clickable
color_filter = wait.until(
    EC.element_to_be_clickable((By.NAME, "color-filter"))
)

# ✅ Blank 3: Apply color filter
color_filter.click()
color_filter.send_keys("Black")
color_filter.send_keys(Keys.ENTER)

# Wait for the product listings to reflect the applied filters
product_listings = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item"))
)

# Apply the price filter
price_filter = driver.find_element(By.ID, "pricefilter")
price_filter.send_keys("500-1000")
price_filter.send_keys(Keys.ENTER)

# ✅ Blank 4: Wait until product listings update after price filter
wait.until(
    lambda driver: len(driver.find_elements(By.CLASS_NAME, "product-item")) > 0
)

# ✅ Blank 5: Assert product listings meet the applied criteria
for product in driver.find_elements(By.CLASS_NAME, "product-item"):
    assert "Black" in product.text
    assert "₹" in product.text

driver.quit()