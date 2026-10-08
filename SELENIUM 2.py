from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://demo.automationtesting.in/Register.html")

print("TC01 - Open Registration Page")
print("Page opened successfully")


username = driver.find_element(
    By.XPATH,
    "//input[@placeholder='First Name']"
)

username.send_keys("ADITHYA V")

print("TC02 - Username entered")


password = driver.find_element(
    By.XPATH,
    "//input[@id='firstpassword']"
)

password.send_keys("Selenium@123")

print("TC03 - Password entered")


submit = driver.find_element(
    By.XPATH,
    "//button[normalize-space(text())='Submit']"
)

print("TC04 - Submit button found")
print(submit.text)


textbox = driver.find_element(
    By.XPATH,
    "//input[contains(@placeholder,'Name')]"
)

print("TC05 - Textbox found using contains()")


lastname = driver.find_element(
    By.XPATH,
    "//input[starts-with(@placeholder,'Last')]"
)

lastname.send_keys("Official")

print("TC06 - Last Name found using starts-with()")


firstname = driver.find_element(
    By.XPATH,
    "//input[@placeholder='First Name' and @type='text']"
)

print("TC07 - Input found using and")


name = driver.find_elements(
    By.XPATH,
    "//input[@placeholder='First Name' or @placeholder='Last Name']"
)

print("TC08 - Elements found using or")
print("Number of elements:", len(name))


parent = driver.find_element(
    By.XPATH,
    "//input[@placeholder='First Name']/parent::*"
)

print("TC09 - Parent found")
print(parent.tag_name)


form = driver.find_element(
    By.XPATH,
    "//input[@placeholder='First Name']/ancestor::form"
)

print("TC10 - Form found using ancestor")
print(form.tag_name)


children = driver.find_elements(
    By.XPATH,
    "//form/child::*"
)

print("TC11 - Child elements found")
print("Number of child elements:", len(children))


following = driver.find_elements(
    By.XPATH,
    "//input[@placeholder='First Name']/following::*"
)

print("TC12 - Following elements found")
print("Number of following elements:", len(following))


checkbox = driver.find_element(
    By.XPATH,
    "//input[@type='checkbox' and @value='Cricket']"
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    checkbox
)

driver.execute_script(
    "arguments[0].click();",
    checkbox
)

print("TC13 - Cricket checkbox selected")


radio = driver.find_element(
    By.XPATH,
    "//input[@type='radio' and @value='Male']"
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    radio
)

driver.execute_script(
    "arguments[0].click();",
    radio
)

print("TC14 - Male radio button selected")


skills = driver.find_element(
    By.XPATH,
    "//select[@id='Skills']"
)

select = Select(skills)

select.select_by_visible_text("Java")

print("TC15 - Java selected from Skills dropdown")


second_textbox = driver.find_element(
    By.XPATH,
    "(//input[@type='text'])[2]"
)

print("TC16 - Second textbox found")


address = driver.find_element(
    By.XPATH,
    "//textarea[contains(@ng-model,'Adress')]"
)

address.send_keys("Chennai")


email = driver.find_element(
    By.XPATH,
    "//input[contains(@ng-model,'Email')]"
)

email.send_keys("adhivivek29@gmail.com")


phone = driver.find_element(
    By.XPATH,
    "//input[@ng-model='Phone']"
)

phone.send_keys("9876543210")


second_password = driver.find_element(
    By.XPATH,
    "//input[@id='secondpassword']"
)

second_password.send_keys("Selenium@123")


submit = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[normalize-space(text())='Submit']"
        )
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    submit
)

submit.click()

time.sleep(2)

print("TC17 - Submit button clicked")
print("Form submission completed")


driver.get("https://demo.automationtesting.in/Register.html")

inputs = driver.find_elements(
    By.XPATH,
    "//form[@id='basicBootstrapForm']//input"
)

print("TC18 - All input fields found")
print("Total inputs:", len(inputs))


email = driver.find_element(
    By.XPATH,
    "//input[contains(@ng-model,'Email')]"
)

print("TC19 - Dynamic Email element found using contains()")


driver.get("https://demo.automationtesting.in/Register.html")


driver.find_element(
    By.XPATH,
    "//input[@placeholder='First Name' and @type='text']"
).send_keys("ADITHYA ")


driver.find_element(
    By.XPATH,
    "//input[@placeholder='Last Name']"
).send_keys("V")


driver.find_element(
    By.XPATH,
    "//textarea[contains(@ng-model,'Adress')]"
).send_keys("Velachery, Chennai")


driver.find_element(
    By.XPATH,
    "//input[contains(@ng-model,'Email')]"
).send_keys("adhivivek29@gmail.com")


driver.find_element(
    By.XPATH,
    "//input[@ng-model='Phone']"
).send_keys("9345543305")


radio = driver.find_element(
    By.XPATH,
    "//input[@type='radio' and @value='Male']"
)

driver.execute_script(
    "arguments[0].click();",
    radio
)


checkbox = driver.find_element(
    By.XPATH,
    "//input[@type='checkbox' and @value='Cricket']"
)

driver.execute_script(
    "arguments[0].click();",
    checkbox
)


skills = driver.find_element(
    By.XPATH,
    "//select[@id='Skills']"
)

Select(skills).select_by_visible_text("Java")


driver.find_element(
    By.XPATH,
    "//input[@id='firstpassword']"
).send_keys("Selenium@123")


driver.find_element(
    By.XPATH,
    "//input[@id='secondpassword']"
).send_keys("Selenium@123")


submit = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[normalize-space(text())='Submit']"
        )
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    submit
)

submit.click()

time.sleep(2)

print("TC20 - Complete Registration Automation")
print("Registration process completed")

input("Press Enter to close browser...")

driver.quit()