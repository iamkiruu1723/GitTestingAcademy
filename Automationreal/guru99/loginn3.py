from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Path to your downloaded ChromeDriver
chrome_driver_path = r"C:\Chromedriversu\chromedriver.exe"  # Use the correct path

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(chrome_driver_path))

# Open the website
driver.get("https://demo.guru99.com/v1/index.php")

# Enter the username
username_field = driver.find_element(By.NAME, "uid")
username_field.send_keys("mngr583363")  # Replace with your actual username

# Enter the password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("YdAjyhU")  # Replace with your actual password

# Submit the form
login_button = driver.find_element(By.NAME, "btnLogin")
login_button.click()

# Pause to observe the result (this is optional)
time.sleep(5)

# Close the browser
driver.quit()
