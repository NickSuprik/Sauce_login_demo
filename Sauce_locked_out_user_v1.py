#This script is intended to:
#Test that basic login functions properly for locked_out_user login for the following URL:
#https://www.saucedemo.com/



from selenium import webdriver
from selenium.webdriver.common.by import By
#selenium script startup stuff for python

driver = webdriver.Chrome()
#Here we start the session in the web browser we want to test

driver.get("https://www.saucedemo.com/")
#Navigate to the webpage we want to test

title = driver.title
#Here we request basic browser info?

driver.implicitly_wait(0.5)
#Synchronizing the code with the current state of the browser is one of the biggest challenges with Selenium, and doing it well is an advanced topic.
#Essentially you want to make sure that the element is on the page before you attempt to locate it and the element is in an interactable state before you attempt to interact with it.
#An implicit wait is rarely the best solution, but it’s the easiest to demonstrate here, so we’ll use it as a placeholder.

username_text_box = driver.find_element(by=By.NAME, value="user-name")
password_text_box = driver.find_element(by=By.NAME, value="password")
submit_button = driver.find_element(by=By.ID, value="login-button") 
#Here we declare the "name" fields that we intend to test
#the first value in each line, before the equal sign we declare here in the script , so it can be WHATEVER we want
#the last value in each line, we must find in the webpage, for example by right clicking the element and clicking "Inspect"
    # Then we go to the Elements tab and use the value from the "name" field for the element(s) we want so that it matches


username_text_box.send_keys("locked_out_user")
password_text_box.send_keys("secret_sauce")
submit_button.click()
#Here we list out the intended inputs for our username and password, as well as the input for the submit button
    
#Below are various username and password values for the test site for reference:
'''Accepted usernames are:
standard_user
locked_out_user
problem_user
performance_glitch_user
error_user
visual_user
Password for all users:
secret_sauce
    
text_box.send_keys("Selenium")
submit_button.click()
'''
    
    
# Now we try to capture the result message displayed after login
# On failure (like locked_out_user), an element with data-test="error" appears.
error_message = driver.find_element(by=By.CSS_SELECTOR, value="[data-test='error']")
print("Login result message:", error_message.text)

# Finally we quit and close the script and the browser session
driver.quit()

