from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip
import re
import time


# =========================================================
# YOUR MOBILE NUMBER
# =========================================================
MOBILE_NUMBER = "9345543305"


# =========================================================
# START CHROME
# =========================================================
options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

# Save Flipkart login session
options.add_argument(
    r"--user-data-dir=C:\selenium\flipkart_profile"
)

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 30)


try:

    # =====================================================
    # STEP 1 - OPEN FLIPKART
    # =====================================================

    print("STEP 1: Opening Flipkart...")

    driver.get(
        "https://www.flipkart.com/"
    )

    time.sleep(5)


    # =====================================================
    # STEP 2 - CLICK LOGIN
    # =====================================================

    print("STEP 2: Clicking Login...")

    login = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Login'] | "
                "//button[normalize-space()='Login']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        login
    )

    print("Login clicked.")

    time.sleep(4)


    # =====================================================
    # STEP 3 - FIND PHONE NUMBER FIELD
    # =====================================================

    print("STEP 3: Finding phone number field...")

    phone_box = None

    selectors = [

        # Most specific first
        "//input[@maxlength='10']",

        "//input[@maxlength='10' and @type='text']",

        "//input[@maxlength='10' and @type='tel']",

        "//input[contains(@placeholder,'Phone')]",

        "//input[contains(@name,'phone')]",

        "//input[contains(@name,'mobile')]",

        "//input[contains(@autocomplete,'tel')]"

    ]


    for xpath in selectors:

        try:

            elements = driver.find_elements(
                By.XPATH,
                xpath
            )

            for element in elements:

                if (
                    element.is_displayed()
                    and element.is_enabled()
                ):

                    phone_box = element

                    print("Phone field found using:")
                    print(xpath)

                    break

            if phone_box is not None:
                break

        except Exception:
            pass


    # =====================================================
    # METHOD 2 - FIND INPUT NEAR PHONE NUMBER LABEL
    # =====================================================

    if phone_box is None:

        print("Trying Phone Number label...")

        try:

            phone_label = driver.find_element(
                By.XPATH,
                "//*[normalize-space()='Phone Number']"
            )

            parents = [

                phone_label.find_element(
                    By.XPATH,
                    "./.."
                ),

                phone_label.find_element(
                    By.XPATH,
                    "../.."
                ),

                phone_label.find_element(
                    By.XPATH,
                    "../../.."
                ),

                phone_label.find_element(
                    By.XPATH,
                    "../../../.."
                )
            ]


            for parent in parents:

                inputs = parent.find_elements(
                    By.TAG_NAME,
                    "input"
                )

                for element in inputs:

                    if (
                        element.is_displayed()
                        and element.is_enabled()
                    ):

                        phone_box = element

                        print(
                            "Phone field found near Phone Number label."
                        )

                        break

                if phone_box is not None:
                    break

        except Exception as e:

            print(
                "Label search failed:",
                e
            )


    # =====================================================
    # PHONE FIELD NOT FOUND
    # =====================================================

    if phone_box is None:

        print()
        print("==============================================")
        print("PHONE FIELD COULD NOT BE LOCATED")
        print("==============================================")

        print(
            "Browser will remain open."
        )

        input(
            "Press ENTER only after inspecting the page..."
        )

    else:

        # =================================================
        # STEP 4 - ENTER MOBILE NUMBER
        # =================================================

        print()
        print(
            "STEP 4: Entering mobile number..."
        )

        # Scroll to phone field
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            phone_box
        )

        time.sleep(1)

        # Click field
        ActionChains(driver).move_to_element(
            phone_box
        ).click().perform()

        time.sleep(0.5)

        # Clear field
        phone_box.clear()

        # Enter mobile number
        phone_box.send_keys(
            MOBILE_NUMBER
        )

        print(
            "Mobile number entered successfully!"
        )

        time.sleep(2)


        # =================================================
        # STEP 5 - CLICK CONTINUE
        # =================================================

        print(
            "STEP 5: Clicking Continue..."
        )

        continue_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[normalize-space()='Continue']"
                )
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        print(
            "Continue clicked."
        )


        # =================================================
        # STEP 6 - WAIT FOR OTP
        # =================================================

        print()
        print("==============================================")
        print("OTP SENT TO YOUR MOBILE")
        print("==============================================")

        print(
            "Copy the OTP from your SMS."
        )

        input(
            "After copying the OTP, press ENTER here..."
        )


        # =================================================
        # STEP 7 - READ OTP FROM WINDOWS CLIPBOARD
        # =================================================

        print(
            "Reading OTP from clipboard..."
        )

        try:

            clipboard_text = (
                pyperclip.paste()
                .strip()
            )

        except Exception as e:

            print(
                "Could not access clipboard:",
                e
            )

            clipboard_text = ""


        # Keep only digits
        otp = re.sub(
            r"\D",
            "",
            clipboard_text
        )


        # =================================================
        # CHECK OTP
        # =================================================

        if len(otp) < 4:

            print()
            print("==============================================")
            print("COULD NOT DETECT A VALID OTP")
            print("==============================================")

            print(
                "Clipboard contents did not contain "
                "a valid OTP."
            )

            # Manual fallback
            otp = input(
                "Enter OTP manually: "
            ).strip()

        else:

            print(
                "OTP detected."
            )


        # =================================================
        # STEP 8 - FIND OTP INPUTS
        # =================================================

        print(
            "STEP 6: Finding OTP fields..."
        )

        time.sleep(1)

        inputs = driver.find_elements(
            By.TAG_NAME,
            "input"
        )

        otp_boxes = []


        for element in inputs:

            try:

                if (
                    not element.is_displayed()
                    or not element.is_enabled()
                ):
                    continue


                maxlength = element.get_attribute(
                    "maxlength"
                )

                inputmode = element.get_attribute(
                    "inputmode"
                )

                placeholder = (
                    element.get_attribute(
                        "placeholder"
                    ) or ""
                ).lower()

                aria_label = (
                    element.get_attribute(
                        "aria-label"
                    ) or ""
                ).lower()


                if (
                    maxlength == "1"
                    or inputmode == "numeric"
                    or "otp" in placeholder
                    or "otp" in aria_label
                ):

                    otp_boxes.append(
                        element
                    )

            except Exception:
                pass


        # =================================================
        # STEP 9 - ENTER OTP
        # =================================================

        print(
            "STEP 7: Entering OTP..."
        )


        # -----------------------------------------------
        # SINGLE OTP FIELD
        # -----------------------------------------------

        if len(otp_boxes) == 1:

            otp_boxes[0].click()

            otp_boxes[0].send_keys(
                otp
            )

            print(
                "OTP entered successfully."
            )


        # -----------------------------------------------
        # MULTIPLE OTP BOXES
        # -----------------------------------------------

        elif len(otp_boxes) >= len(otp):

            for i, digit in enumerate(otp):

                otp_boxes[i].click()

                otp_boxes[i].send_keys(
                    digit
                )

            print(
                "OTP entered into separate boxes."
            )


        # -----------------------------------------------
        # OTP BOXES NOT FOUND
        # -----------------------------------------------

        else:

            print()
            print(
                "OTP boxes not detected."
            )

            print(
                "Please enter OTP manually in Chrome."
            )

            input(
                "After entering OTP, press ENTER..."
            )


        # =================================================
        # STEP 10 - CLICK VERIFY
        # =================================================

        time.sleep(1)

        print(
            "STEP 8: Clicking Verify..."
        )

        try:

            verify = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[normalize-space()='Verify']"
                    )
                )
            )

            driver.execute_script(
                "arguments[0].click();",
                verify
            )

            print(
                "Verify clicked."
            )

        except Exception:

            print(
                "Verify button was not detected."
            )

            print(
                "Please click Verify manually."
            )


        # =================================================
        # STEP 11 - WAIT FOR LOGIN
        # =================================================

        time.sleep(5)


        print()
        print("==============================================")
        print("FLIPKART LOGIN COMPLETED")
        print("==============================================")

        print(
            "Current URL:",
            driver.current_url
        )


        # Keep browser open
        input(
            "\nPress ENTER to close Chrome..."
        )


# =========================================================
# ERROR HANDLING
# =========================================================

except Exception as e:

    print()
    print("==============================================")
    print("ERROR")
    print("==============================================")

    print(
        type(e).__name__
    )

    print(
        str(e)
    )

    print()
    print(
        "Chrome will remain open."
    )

    input(
        "Press ENTER to close Chrome..."
    )


# =========================================================
# CLOSE BROWSER
# =========================================================

finally:

    try:
        driver.quit()
    except:
        pass
    