#This script is intended to:
#Test that basic login functions properly for locked_out_user and standard_user on:
#https://www.saucedemo.com/

#powershell line to run script:
#python Sauce_script_v3_loop.py

'''
Accepted usernames are:
standard_user
locked_out_user
problem_user
performance_glitch_user
error_user
visual_user
Password for all users:
secret_sauce
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import tempfile

# ---- ADD THIS RIGHT AFTER YOUR IMPORTS ----
options = Options()



# Disable password manager + leak detection popup
prefs = {
    "reduce-security-for-testing": True,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
    "profile.default_content_setting_values.notifications": 2
}
options.add_experimental_option("prefs", prefs)

# Disable Chrome features that trigger the warning
options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,SafeBrowsingEnhancedProtection")
options.add_argument("--disable-infobars")
options.add_argument("--password-store=basic")
options.add_argument("--disable-notifications")
options.add_argument("--disable-save-password-bubble")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-blink-features=AutomationControlled")

# (Optional) create a temporary fresh Chrome profile each run
temp_profile = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={temp_profile}")

# Initialize WebDriver with the new options
driver = webdriver.Chrome(options=options)


#SauceDemo Start
users = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]

for user in users:

    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(0.5)

    username_text_box = driver.find_element(by=By.NAME, value="user-name")
    password_text_box = driver.find_element(by=By.NAME, value="password")
    submit_button = driver.find_element(by=By.ID, value="login-button")
    

    username_text_box.send_keys(user)
    password_text_box.send_keys("secret_sauce")
    submit_button.click()


    # Wait for either success, error message or redirect
    try:
        error_el = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error'], .error-message-container"))
        )
        error_text = error_el.text.strip()
        print(f"[{user} Login Test]")
        print("! Login produced an error message:")
        print(error_text)
        print(" ")
    except TimeoutException:
        # If no error appears, check for success
        current_url = driver.current_url
        print(f"[{user} Login Test]")
        if "inventory.html" in current_url:
            print(":) Login successful! Reached inventory page.")
            print(" ")
        else:
            print("!! No error message or redirect detected.")
            print("Current URL:", current_url)
            print("Page title:", driver.title)
            print(" ")


#SauceDemo End


# Finally we quit and close the script and the browser session
driver.quit()
