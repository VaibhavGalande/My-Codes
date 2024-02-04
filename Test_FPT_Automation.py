# Import necessary modules from the framework
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the browser
driver = webdriver.Chrome("D:\chromedriver.exe")

# Open the website
driver.get("http://practice.automationtesting.in/")

# Click on My Account Menu
my_account_menu = driver.find_element(By.LINK_TEXT, "My Account")
my_account_menu.click()

# Enter registered username and password
username = driver.find_element(By.ID, "vaibhavgalande11@gmail.com")
password = driver.find_element(By.ID, "Jaguar@12345")
username.send_keys("your_username")
password.send_keys("your_password")

# Click on login button
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# Click on My Account link leading to Dashboard
my_account_link = driver.find_element(By.LINK_TEXT, "My Account")
my_account_link.click()

# Check if user is on the Dashboard
dashboard_title = driver.title
if "Dashboard" in dashboard_title:
    print("Successfully logged in and on the Dashboard")
else:
    print("Login unsuccessful or Dashboard not reached")

# Close the browser
driver.quit()
