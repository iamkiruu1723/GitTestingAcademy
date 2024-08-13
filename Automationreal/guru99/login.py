from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


chrome_driver_pathuu = r"C:\Chromedriversu\chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_pathuu))

driver.maximize_window()


driver.get("https://demo.guru99.com/v1/index.php")

username_field = driver.find_element(By.NAME, "uid")
username_field.send_keys("mngr583363")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("YdAjyhU")

login_button = driver.find_element(By.NAME, "btnLogin")
login_button.click()

time.sleep(5)

driver.get("https://demo.guru99.com/v1/html/addcustomerpage.php")

cmr_name = driver.find_element(By.NAME, "name")
cmr_name.send_keys("kirannuuuuaas")
#
cmr_name = driver.find_element(By.NAME, "rad")
cmr_name.send_keys("1")

cmr_dob = driver.find_element(By.NAME, "dob")
cmr_dob.send_keys("08/07/1997")

cmr_addrs = driver.find_element(By.NAME, "addr")
cmr_addrs.send_keys("sunkadakttee")

city = driver.find_element(By.NAME, "city")
city.send_keys("bengaluru")

pincode = driver.find_element(By.NAME, "pinno")
pincode.send_keys("566011")

mobno= driver.find_element(By.NAME, "telephoneno")
mobno.send_keys("876123456")

emailu = driver.find_element(By.NAME, "emailid")
emailu.send_keys("kiranuu@gmail.com")

stateu= driver.find_element(By.NAME,"state")
stateu.send_keys("karunaddu")

# login_buttonu = driver.find_element(By.NAME, "sub")
# login_buttonu.click()


time.sleep(50)


