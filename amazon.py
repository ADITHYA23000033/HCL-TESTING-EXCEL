from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

def find_click(selectors):
    for by, value in selectors:
        try:
            e = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((by, value))
            )
            if e.is_displayed():
                driver.execute_script("arguments[0].click();", e)
                return True
        except:
            pass
    return False

driver.get("https://www.amazon.in/")
driver.maximize_window()

search = wait.until(
    EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
)
search.send_keys("wireless mouse")
search.send_keys(Keys.ENTER)

products = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@data-component-type='s-search-result']")
    )
)

added = False

for p in products:
    try:
        link = p.find_element(
            By.XPATH,
            ".//a[contains(@href,'/dp/') or contains(@href,'/gp/product/')]"
        )
        driver.get(link.get_attribute("href"))

        if find_click([
            (By.ID, "add-to-cart-button"),
            (By.NAME, "submit.add-to-cart"),
            (By.ID, "add-to-cart-button-ubb"),
            (By.CSS_SELECTOR, "input[value='Add to Cart']"),
            (By.CSS_SELECTOR, "input[title='Add to Shopping Cart']")
        ]):
            added = True
            break
    except:
        pass

if not added:
    print("Add to Cart failed")
    driver.quit()
    exit()

find_click([(By.ID, "nav-cart")])

if not find_click([
    (By.NAME, "proceedToRetailCheckout"),
    (By.XPATH, "//input[contains(@name,'proceedToRetailCheckout')]"),
    (By.XPATH, "//span[contains(.,'Proceed to Buy')]/ancestor::a[1]"),
    (By.XPATH, "//span[contains(.,'Proceed to Buy')]/ancestor::button[1]"),
    (By.ID, "sc-buy-box-ptc-button")
]):
    print("Proceed to Buy failed")
    driver.quit()
    exit()

wait.until(lambda d: "signin" in d.current_url.lower())

print("Amazon login page opened")
print("Automation stopped")

input("Press ENTER to close...")
driver.quit()