from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin

# -------------------------------
# START BROWSER
# -------------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------
# OPEN TARGET WEBSITE
# -------------------------------
url = "https://example.com"   # Replace with your target site
driver.get(url)

# -------------------------------
# FIND ALL <a> TAGS
# -------------------------------
links = driver.find_elements(By.TAG_NAME, "a")

print(f"Total links found: {len(links)}")

broken_links = []
working_links = []

# -------------------------------
# CHECK EACH LINK
# -------------------------------
for link in links:
    href = link.get_attribute("href")

    # Ignore empty or javascript links
    if href is None or href.strip() == "" or href.startswith("javascript"):
        continue

    # Handle relative URLs
    full_url = urljoin(url, href)

    try:
        response = requests.head(full_url, timeout=5)

        if response.status_code >= 400:
            broken_links.append((full_url, response.status_code))
        else:
            working_links.append((full_url, response.status_code))

    except requests.exceptions.RequestException:
        broken_links.append((full_url, "Request Failed"))

# -------------------------------
# PRINT RESULTS
# -------------------------------
print("\n✅ Working Links:")
for link, status in working_links:
    print(f"{link} --> {status}")

print("\n❌ Broken Links:")
for link, status in broken_links:
    print(f"{link} --> {status}")

print("\nSUMMARY")
print("--------")
print("Total links checked:", len(working_links) + len(broken_links))
print("Working links:", len(working_links))
print("Broken links:", len(broken_links))

# -------------------------------
# CLOSE BROWSER
# -------------------------------
driver.quit()