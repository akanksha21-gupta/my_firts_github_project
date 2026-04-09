from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Initialize WebDriverWait with 15 seconds
        self.wait = WebDriverWait(driver, 15)


class HomePage(BasePage):
    def go_to_category(self):
        # Wait until category button is clickable
        category_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "categoryButton"))
        )
        category_button.click()


class CategoryPage(BasePage):
    def select_course(self):
        # Wait for course list to be visible
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "course-title"))
        )
        course = self.driver.find_element(By.CLASS_NAME, "course-title")
        course.click()


class CoursePage(BasePage):
    def enroll(self):
        enroll_button = self.driver.find_element(By.ID, "enrollButton")
        enroll_button.click()

        # Verify redirection to login
        self.wait.until(
            EC.url_contains("login")
        )


def test_enrollment_requires_login():
    driver = webdriver.Chrome()
    home = HomePage(driver)

    driver.get("https://eduplatform.com")

    home.go_to_category()

    category = CategoryPage(driver)
    category.select_course()

    course = CoursePage(driver)
    course.enroll()

    # Assert URL contains login
    assert "login" in driver.current_url

    driver.quit()