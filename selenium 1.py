from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# SETUP
# ============================================================

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)


# ============================================================
# ALERT
# ============================================================

print("\n========== ALERT ==========")


# ============================================================
# TC01 - ALERT ACCEPT
# ============================================================

print("\nTC01 - Alert Accept")

driver.get(
    "https://the-internet.herokuapp.com/javascript_alerts"
)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Confirm']")
    )
).click()

alert = wait.until(
    EC.alert_is_present()
)

print("Alert Message:", alert.text)

alert.accept()

print("PASS - Alert accepted successfully")


# ============================================================
# TC02 - ALERT DISMISS
# ============================================================

print("\nTC02 - Alert Dismiss")

driver.get(
    "https://the-internet.herokuapp.com/javascript_alerts"
)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Confirm']")
    )
).click()

alert = wait.until(
    EC.alert_is_present()
)

print("Alert Message:", alert.text)

alert.dismiss()

print("PASS - Alert dismissed successfully")


# ============================================================
# TC03 - PROMPT
# ============================================================

print("\nTC03 - Prompt")

driver.get(
    "https://the-internet.herokuapp.com/javascript_alerts"
)

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Prompt']")
    )
).click()

alert = wait.until(
    EC.alert_is_present()
)

print("Prompt Message:", alert.text)

alert.send_keys("Vimala")

alert.accept()

print("PASS - Prompt information entered successfully")


# ============================================================
# WAIT
# ============================================================

print("\n========== WAIT ==========")


# ============================================================
# TC04 - VISIBILITY WAIT
# ============================================================

print("\nTC04 - Visibility Wait")

driver.get(
    "https://www.saucedemo.com/"
)

username = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "user-name")
    )
)

username.send_keys("standard_user")

print("PASS - Username field found using Explicit Wait")


# ============================================================
# TC05 - CLICKABLE WAIT
# ============================================================

print("\nTC05 - Clickable Wait")

password = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "password")
    )
)

password.send_keys("secret_sauce")

login_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "login-button")
    )
)

login_button.click()

print("PASS - Login button clicked using Explicit Wait")


# ============================================================
# TC06 - WAIT FOR PRODUCT PAGE
# ============================================================

print("\nTC06 - Wait for Product Page")

product_page = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "title")
    )
)

print("Page:", product_page.text)

print("PASS - Product page loaded using Explicit Wait")


# ============================================================
# DROPDOWN
# ============================================================

print("\n========== DROPDOWN ==========")


# ============================================================
# TC07 - SELECT BY VISIBLE TEXT
# ============================================================

print("\nTC07 - Select By Visible Text")

driver.get(
    "https://the-internet.herokuapp.com/dropdown"
)

dropdown = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "dropdown")
    )
)

select = Select(dropdown)

select.select_by_visible_text("Option 1")

print(
    "Selected:",
    select.first_selected_option.text
)

print("PASS - Dropdown selected using visible text")


# ============================================================
# TC08 - SELECT BY VALUE
# ============================================================

print("\nTC08 - Select By Value")

select.select_by_value("2")

print(
    "Selected:",
    select.first_selected_option.text
)

print("PASS - Dropdown selected using value")


# ============================================================
# TC09 - SELECT BY INDEX
# ============================================================

print("\nTC09 - Select By Index")

select.select_by_index(1)

print(
    "Selected:",
    select.first_selected_option.text
)

print("PASS - Dropdown selected using index")


# ============================================================
# TC10 - DISPLAY ALL OPTIONS
# ============================================================

print("\nTC10 - Display All Dropdown Options")

options = select.options

for option in options:
    print(option.text)

print("PASS - All dropdown options displayed")


# ============================================================
# FINAL RESULT
# ============================================================

print("\n========================================")
print("ALL 10 TEST CASES COMPLETED")
print("========================================")

input("\nPress Enter to close...")

driver.quit()


## https://github.com/ADITHYA23000033/HCL-TESTING-EXCEL/edit/main/selenium%201.py
