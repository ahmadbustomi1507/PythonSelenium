from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import copy

import time

#Pre initialization
PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)
action_driver = webdriver.ActionChains(driver)

Username  = 'tomi'
Password  = 'P@ssw0rd.'
user_name_path = "//input[@name='username']"
user_password_path = "//input[@name='password']"

# Start
try:
    driver.maximize_window()
    driver.get("https://cybersmart.predictintel.ai/cpq496wk65/#/")

    login_page_element = WebDriverWait(driver,60).until(
        EC.visibility_of_element_located(
            (By.XPATH,"//input[@name='username']")
        )
    )
    user_name_element = WebDriverWait(driver,60).until(
        EC.element_to_be_clickable(
            (By.XPATH,user_name_path)
        )
    )

    user_password_element = WebDriverWait(driver,60).until(
        EC.element_to_be_clickable(
            (By.XPATH, user_password_path)
        )
    )
    user_name = driver.find_element_by_xpath(user_name_path)
    user_name.send_keys(Username)
    user_password = driver.find_element_by_xpath(user_password_path)
    user_password.send_keys(Password)

    driver.find_element_by_xpath("//button[contains(@class,'login-btn')]").click()

except:
    print('Ga keluar page nya bray... rerun lagi aja, hadeh')
    driver.quit()

try:


    element = WebDriverWait(driver,60).until(
        EC.visibility_of_element_located(
            (By.ID,"main-content")
        )
    )

    locator_by_link = driver.find_element_by_link_text("Entity/Case Management")
    locator_menu    = locator_by_link.find_element_by_xpath("..")

finally:
    menu_for_test = copy.copy(locator_menu)

action_driver.move_to_element(menu_for_test)
action_driver.perform()
sub_menu_cases=menu_for_test.find_elements_by_xpath("//menu[contains(@data-v-,'')]/li")

#locate the case
for sub_menu_case in sub_menu_cases:
    if "Case" in sub_menu_case.text:
        action_driver.move_to_element(sub_menu_case)
        action_driver.click()
        action_driver.perform()
        break


# a