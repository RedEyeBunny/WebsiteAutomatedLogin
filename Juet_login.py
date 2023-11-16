from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()

driver.get("https://webkiosk.juet.ac.in/")
time.sleep(2)

# for student's login
select = Select(driver.find_element(By.ID, "UserType"))
select.select_by_index(0)

En_ro = driver.find_element(By.ID, "MemberCode")
En_ro.send_keys("Your Enrollment Number")

dob = driver.find_element(By.ID, "DATE1")
dob.send_keys("Your birthdate")

password = driver.find_element(By.ID, "Password")
password.send_keys("Your password")

captcha = driver.find_element(By.ID, "txtcap")
cap_text = driver.find_element(By.CLASS_NAME, "noselect").text
captcha.send_keys(cap_text)

submit_btn = driver.find_element(By.ID, "BTNSubmit")
submit_btn.click()

