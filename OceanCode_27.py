from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://website.com/blog')
posts_data = []

try:
    # Blank 1: Wait for the posts to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'post'))
    )
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

# Blank 2: Find all posts
posts = driver.find_elements(By.CLASS_NAME, 'post')

for post in posts:
    try:
        # Extract title, author, and content
        title = post.find_element(By.TAG_NAME, 'h2').text
        author = post.find_element(By.CLASS_NAME, 'author').text
        content = post.find_element(By.CLASS_NAME, 'content').text
    except NoSuchElementException: # Blank 3: Handle missing elements
        print("One of the elements was not found. Moving to next post.")
        continue
    # Blank 4: Append data to the list
    posts_data.append({'title': title, 'author': author, 'content': content})

# Blank 5: Write data to a JSON file
with open('posts_data.json', 'w') as f:
    json.dump(posts_data, f, ensure_ascii=False, indent=4)

driver.quit()