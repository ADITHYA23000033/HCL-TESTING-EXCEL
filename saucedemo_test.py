from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("actor Simbu")
search.send_keys(Keys.ENTER)

input("Press Enter to close...")
driver.quit()