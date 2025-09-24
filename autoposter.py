import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv()
FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")

BLOG_POST_CONTENT = """
Success! :)

This post was created with a fixed script. Debugging selectors and character encoding are key skills in web automation. This now works perfectly.

#Python #Selenium #Automation #Fixed
"""


print("🚀 Starting the Facebook Auto Poster...")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)
wait = WebDriverWait(driver, 30) 

try:
   
    driver.get("https://www.facebook.com")
    driver.maximize_window()

    
    print("Logging in...")
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    pass_field = driver.find_element(By.ID, "pass")
    
    email_field.send_keys(FACEBOOK_EMAIL)
    pass_field.send_keys(FACEBOOK_PASSWORD)
    driver.find_element(By.NAME, "login").click()
    
    print("\n--- ACTION REQUIRED ---")
    input("Please solve any CAPTCHA or puzzle and close any popups (like 'Save login info').\nOnce you see the main Facebook feed, press the Enter key in this terminal to continue...")
    
    print("\n✅ Resuming automation...")

    
    post_box_xpath = "//*[contains(text(), \"What's on your mind\")]"
    whats_on_your_mind = wait.until(EC.element_to_be_clickable((By.XPATH, post_box_xpath)))
    whats_on_your_mind.click()
    print("Clicked on 'What's on your mind?'.")

    
    post_textarea_xpath = "//div[@role='dialog']//div[@role='textbox']"
    post_textarea = wait.until(EC.visibility_of_element_located((By.XPATH, post_textarea_xpath)))
    
    post_textarea.send_keys(BLOG_POST_CONTENT)
    print("✍️ Blog content has been entered.")
    time.sleep(2)

    
    post_button_xpath = "//div[@aria-label='Post']//span[text()='Post']"
    post_button = wait.until(EC.element_to_be_clickable((By.XPATH, post_button_xpath)))
    post_button.click()
    print("🎉 Post published successfully!")

    time.sleep(5)

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    
    print("Closing the browser.")
    driver.quit()