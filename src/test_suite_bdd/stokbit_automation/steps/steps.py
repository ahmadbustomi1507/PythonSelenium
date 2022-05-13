# from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb
import time

@given(u'do something')
def step_impl(context):

    context.feature.driver.get(context.feature.base_web)
    # print('given success')
    el = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME,'login-ldn'))
    login = context.feature.driver.find_element(By.CLASS_NAME,'login-ldn')
    login.click()

    el = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.ID,'form-login'))
    form_login = context.feature.driver.find_element(By.ID,'form-login')

    username = form_login.find_element(By.ID,'username')
    username.clear()
    username.send_keys('ahmadbustomi1507@gmail.com')

    password = form_login.find_element(By.ID,'password')
    password.clear()
    password.send_keys('tu4nt0m1')

    submit =  context.feature.driver.find_element(By.ID,'loginbutton')
    submit.click()

    # Get the announcement pop up
    try:
        el              = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.XPATH,"//div[contains(@class,'announcement-modal')]"))
        profile_avatar  = context.feature.driver.find_element(By.XPATH,"//div[contains(@class,'announcement-modal')]")
    except Exception as err:
        print('selector not found ')
    finally:
        # style_attribute = profile_avatar.get_attribute('style')
        # print(f'style_attribute {style_attribute} type {type(style_attribute)}')

        profile_avatar_buttons    = profile_avatar.find_elements(By.TAG_NAME,'button')
        for button in profile_avatar_buttons:
            if button.text == "Skip":
                skip_button = button
            elif button.text == "Choose Avatar":
                choose_avatar_button = button
        skip_button.click()

    context.feature.driver.implicitly_wait(5)
    # profile_avatar  = context.feature.driver.find_element(By.XPATH,"//div[contains(@class,'announcement-modal')]")
    # style_attribute = profile_avatar.get_attribute('style')
    # print(f'style_attribute {style_attribute} type {type(style_attribute)}')



@when(u'do when')
def step_impl(context):
    el = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.ID,'watchlistLink'))
    watchlist_menu = context.feature.driver.find_element(By.ID,'watchlistLink')
    watchlist_menu.click()

    # watchlist_add_box = context.feature.driver.find_element(By.XPATH,"//input[contains(@placeholder,'Type here to add companies')]")
    el = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.XPATH,"//input[contains(@placeholder,'Type here to add companies')]"))

    # TO DO
    context.feature.driver.execute_script('''
        function getElementByXpath(path) {
          return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        };      
        var xPath             = "//input[contains(@placeholder,'Type here to add companies')]";
        var watchlist_add_box = getElementByXpath(xPath);
        watchlist_add_box.value='ADRO';
    ''')
    pdb.set_trace()
    print('when success')


@then(u'do then')
def step_impl(context):
    context.feature.driver.quit()
    pass