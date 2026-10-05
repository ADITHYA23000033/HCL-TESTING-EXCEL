from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login.click()

products = driver.find_elements(By.CLASS_NAME, "inventory_item")

for product in products[:5]:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    print("Product:", name)
    print("Price:", price)
    print()

input("Press Enter to close...")
driver.quit()