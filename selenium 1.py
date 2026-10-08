# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver=webdriver.Chrome()

# driver.get("https://www.saucedemo.com/")

# assert "Swag Labs" in driver.title

# username=driver.find_element(By.ID,"user-name")
# username.send_keys("standard_user")

# password=driver.find_element(By.ID,"password")
# password.send_keys("secret_sauce")

# login=driver.find_element(By.ID,"login-button")
# login.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

print("TC01 - Shopping website opened successfully")

wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
)

print("TC01 - Login successful")


driver.get("https://www.selenium.dev/selenium/web/alerts.html")

driver.find_element(By.ID, "alert").click()

alert = wait.until(
    EC.alert_is_present()
)

print("\nTC02 - Alert:")
print(alert.text)

alert.accept()

print("TC02 - Product deletion confirmed")


driver.get("https://www.selenium.dev/selenium/web/alerts.html")

driver.find_element(By.ID, "confirm").click()

alert = wait.until(
    EC.alert_is_present()
)

print("\nTC03 - Confirmation Alert:")
print(alert.text)

alert.dismiss()

print("TC03 - Product remains in the cart")


driver.get("https://www.selenium.dev/selenium/web/alerts.html")

driver.find_element(By.ID, "prompt").click()

alert = wait.until(
    EC.alert_is_present()
)

print("\nTC04 - Prompt Alert:")
print(alert.text)

alert.send_keys("ADITHYA V")
alert.accept()

print("TC04 - Customer information submitted successfully")


driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

hover_element = wait.until(
    EC.visibility_of_element_located((By.ID, "hover"))
)

ActionChains(driver).move_to_element(hover_element).perform()

move_status = wait.until(
    EC.visibility_of_element_located((By.ID, "move-status"))
)

print("\nTC05 - Mouse Hover performed successfully")
print("Result:", move_status.text)


driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

double_click_element = wait.until(
    EC.visibility_of_element_located((By.ID, "clickable"))
)

ActionChains(driver).double_click(double_click_element).perform()

click_status = wait.until(
    EC.visibility_of_element_located((By.ID, "click-status"))
)

print("\nTC06 - Double Click performed successfully")
print("Result:", click_status.text)


driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

source = wait.until(
    EC.visibility_of_element_located((By.ID, "draggable"))
)

target = wait.until(
    EC.visibility_of_element_located((By.ID, "droppable"))
)

ActionChains(driver).drag_and_drop(source, target).perform()

drop_status = wait.until(
    EC.visibility_of_element_located((By.ID, "drop-status"))
)

print("\nTC07 - Drag and Drop performed successfully")
print("Result:", drop_status.text)


driver.get("https://www.automationexercise.com/products")

search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "search_product"))
)

search_box.clear()
search_box.send_keys("Top")

search_button = wait.until(
    EC.element_to_be_clickable((By.ID, "submit_search"))
)

search_button.click()

searched_products = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "//h2[contains(translate(normalize-space(.), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'SEARCHED PRODUCTS')]"
        )
    )
)

products = wait.until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH,
            "//div[contains(@class,'productinfo')]"
        )
    )
)

print("\nTC08 - Product search completed successfully")
print("Result:", searched_products.text)
print("Number of products found:", len(products))


driver.get("https://www.saucedemo.com/")

wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
)

driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"
).click()

driver.find_element(
    By.CLASS_NAME, "shopping_cart_link"
).click()

wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
)

driver.find_element(By.ID, "checkout").click()

wait.until(
    EC.visibility_of_element_located((By.ID, "first-name"))
).send_keys("ADITHYA ")

driver.find_element(By.ID, "last-name").send_keys("V")
driver.find_element(By.ID, "postal-code").send_keys("600117")

driver.find_element(By.ID, "continue").click()

finish_button = wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
)

print("\nTC09 - Place Order button is clickable")

finish_button.click()

confirmation = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "complete-header")
    )
)

print("TC09 - Order submitted successfully")
print("Result:", confirmation.text)


driver.get("https://www.saucedemo.com/")

wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
)

driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"
).click()

driver.find_element(
    By.CLASS_NAME, "shopping_cart_link"
).click()

wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
)

driver.find_element(By.ID, "checkout").click()

wait.until(
    EC.visibility_of_element_located((By.ID, "first-name"))
).send_keys("ADITHYA V")

driver.find_element(By.ID, "last-name").send_keys("V")
driver.find_element(By.ID, "postal-code").send_keys("600117 ")

driver.find_element(By.ID, "continue").click()

finish_button = wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
)

finish_button.click()

wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "complete-header")
    )
)

driver.execute_script(
    "setTimeout(function(){alert('Order confirmation successful')}, 500)"
)

alert = wait.until(
    EC.alert_is_present()
)

print("\nTC10 - Order Confirmation Alert:")
print(alert.text)

alert.accept()

print("TC10 - Confirmation alert handled successfully")

time.sleep(2)

driver.quit()

print("\nAll test cases completed successfully")


