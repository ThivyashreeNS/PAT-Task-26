# Import necessary libraries for web automation using Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Task_26.Resources.Data import Data
from Task_26.Resources.Locators import Locators

class ImdbSearch(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set an explicit wait to wait for elements to become interactable (up to 10 seconds)
        self.wait = WebDriverWait(self.driver, 20)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def imdb_search(self):
        try:
            # Scroll down to load content
            for _ in range(12):
                self.action.send_keys(Keys.DOWN).perform()

            # Input search name
            name_box = self.wait.until(EC.presence_of_element_located((By.XPATH, self.name)))
            name_box.click()
            input_name = self.wait.until(EC.presence_of_element_located((By.NAME, self.name_input_box)))
            input_name.send_keys(self.search_name)
            print("Name entered successfully")

            # Scroll down to load content
            for _ in range(5):
                self.action.send_keys(Keys.DOWN).perform()

            # Input Birthday field
            birthday_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.birthday)))
            birthday_field.click()
            input_birthday = self.wait.until(EC.presence_of_element_located((By.NAME, self.birthday_input_box)))
            input_birthday.send_keys(self.dob)
            print("Birthday entered successfully")

            # Scroll down to load content
            for _ in range(5):
                self.action.send_keys(Keys.DOWN).perform()

            # Input Gender field
            gender_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.gender_identity)))
            # Scroll to the element
            self.action.move_to_element(gender_field).perform()
            gender_field.click()
            search_gender = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.gender_input)))
            # Scroll to the element
            self.action.move_to_element(search_gender).perform()  # Scroll to the element
            search_gender.click()
            print("Gender entered successfully")

            # Scroll UP to avoid ElementClickInterceptedException
            for _ in range(12):
                self.action.send_keys(Keys.UP).perform()

            # Click See Results button
            see_results = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.see_results_button)))
            see_results.click()
            print("Search success")

            # return the current url of the website after search
            return self.driver.current_url

        # Return any exceptions encountered
        except Exception as error:
            print("Error extracting counts:", error)
            return error

    def close_driver(self):
        """Close the driver"""
        self.driver.quit()
