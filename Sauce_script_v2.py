#This script is intended to:
#Test that basic login functions properly for locked_out_user and standard_user on:
#https://www.saucedemo.com/

#powershell line to run script:
#python Sauce_script_v2.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#selenium script startup stuff for python

driver = webdriver.Chrome()
#Here we start the session in the web browser we want to test


#SauceDemo LockedOutUser Start
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(0.5)

username_text_box = driver.find_element(by=By.NAME, value="user-name")
password_text_box = driver.find_element(by=By.NAME, value="password")
submit_button = driver.find_element(by=By.ID, value="login-button")

username_text_box.send_keys("locked_out_user")
password_text_box.send_keys("secret_sauce")
submit_button.click()

# Wait for either error message or redirect
try:
    error_el = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error'], .error-message-container"))
    )
    error_text = error_el.text.strip()
    print("\n[Locked Out User Test]")
    print("! Login produced an error message:")
    print(error_text)
except TimeoutException:
    print("\n[Locked Out User Test]")
    print("!! No visible error element found. Check if login succeeded or selector needs updating.")
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)

#SauceDemo LockedOutUser End


#SauceDemo StandardUser Start
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(0.5)

username_text_box = driver.find_element(by=By.NAME, value="user-name")
password_text_box = driver.find_element(by=By.NAME, value="password")
submit_button = driver.find_element(by=By.ID, value="login-button")

username_text_box.send_keys("standard_user")
password_text_box.send_keys("secret_sauce")
submit_button.click()

# Wait for either success or error message
try:
    error_el = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error'], .error-message-container"))
    )
    error_text = error_el.text.strip()
    print("\n[Standard User Test]")
    print("! Login produced an error message:")
    print(error_text)
except TimeoutException:
    # If no error appears, check for success
    current_url = driver.current_url
    print("\n[Standard User Test]")
    if "inventory.html" in current_url:
        print(":) Login successful! Reached inventory page.")
    else:
        print("!! No error message or redirect detected.")
        print("Current URL:", current_url)
        print("Page title:", driver.title)

#SauceDemo StandardUser End


# Finally we quit and close the script and the browser session
driver.quit()
