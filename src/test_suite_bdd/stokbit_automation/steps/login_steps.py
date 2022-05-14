
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import copy

@given(u'User successfully navigate to the home page')
def step_impl(context):
    context.feature.driver.get(context.feature.base_web)


@when(u'User click the sign in button')
def step_impl(context):
    el = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, 'login-ldn'))
    login = context.feature.driver.find_element(By.CLASS_NAME, 'login-ldn')
    login.click()

@when('User fill in the "{username}" and "{password}"')
def step_impl(context,username,password):
    el = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.ID,'form-login'))
    form_login = context.feature.driver.find_element(By.ID,'form-login')
    username_selector = form_login.find_element(By.ID,'username')
    username_selector.clear()
    username_selector.send_keys(username)

    password_selector = form_login.find_element(By.ID,'password')
    password_selector.clear()
    password_selector.send_keys(password)

    submit_selector =  context.feature.driver.find_element(By.ID,'loginbutton')
    submit_selector.click()

@then(u'User successfully login with avatar settings pop up')
def step_impl(context):
    # Get the announcement pop up
    try:
        el                           = WebDriverWait(context.feature.driver, timeout=5).until(lambda d: d.find_element(By.XPATH,"//div[contains(@class,'announcement-modal')]"))
        profile_avatar               = context.feature.driver.find_element(By.XPATH,"//div[contains(@class,'announcement-modal')]")
        profile_avatar_buttons       = profile_avatar.find_elements(By.TAG_NAME,'button')
        for button in profile_avatar_buttons:
            if button.text == "Skip":
                skip_button = button
            elif button.text == "Choose Avatar":
                choose_avatar_button = button
        skip_button.click()
    except NoSuchElementException :
        print( 'Announcement pop up not found')
        assert  False,'Announcement pop up is not found'

    except Exception as err:
        print('Something error when looking for announcement pop up')
    finally:
        context.feature.driver.implicitly_wait(5)


@then(u'redirect to the dashboard')
def step_impl(context):
    print(u'STEP: Then redirect to the dashboard')
    el = WebDriverWait(context.feature.driver, timeout=5).until(
        lambda d: d.find_element(By.ID, "homeLink"))
    assert el.text == 'Stream','Not in dashboard'
    context.dashboard = context.feature.driver.find_element(By.ID,"homeLink")



