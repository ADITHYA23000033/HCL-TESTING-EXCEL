from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()

driver.get("https://vinothqaacademy.com/demo-site/")

time.sleep(10)

driver.find_element(By.ID, "vfb-5").send_keys("ADITHYA V")
driver.find_element(By.ID, "vfb-7").send_keys("K")

driver.execute_script(
    "arguments[0].click();",
    driver.find_element(By.ID, "vfb-31-1")
)

driver.execute_script(
    "arguments[0].click();",
    driver.find_element(By.ID, "vfb-20-4")
)

driver.find_element(By.ID, "vfb-13-address").send_keys("ARAKKONAM")
driver.find_element(By.ID, "vfb-13-address-2").send_keys("No: 291/1, 1st Street")
driver.find_element(By.ID, "vfb-13-city").send_keys("Say My Name")
driver.find_element(By.ID, "vfb-13-state").send_keys("Tamil Nadu")
driver.find_element(By.ID, "vfb-13-zip").send_keys("631001")

Select(
    driver.find_element(By.ID, "vfb-13-country")
).select_by_visible_text("India")

driver.find_element(By.ID, "vfb-14").send_keys("ligneshwar2006@gmail.com")
driver.find_element(By.ID, "vfb-18").send_keys("11/09/2006")

time.sleep(10)