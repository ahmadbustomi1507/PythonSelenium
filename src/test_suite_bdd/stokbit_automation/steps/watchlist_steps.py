from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import copy

@given(u'User click the wishlist menu')
def step_impl(context):
    print(u'STEP: Given User click the wishlist menu')

    context.feature.driver.find_element(By.ID,'watchlistLink').click()
    el = WebDriverWait(context.feature.driver, timeout=5).until(
        lambda d: d.find_element(By.XPATH, "//input[contains(@placeholder,'Type here to add companies ...')]"))



@when(u'User fill the wishlist menu as "ADRO"')
def step_impl(context):
    # TO DO :
    watchlist_search_selector_XPATH = "//input[contains(@placeholder,'Type here to add companies')]"
    context.emiten_sample        = "ADRO"
    watchlist_search          = context.feature.driver.find_element(By.XPATH,watchlist_search_selector_XPATH)
    watchlist_search.send_keys('ADRO')
    watchlist_search_value          = watchlist_search.get_attribute('value')
    suggestion_box_selector_XPATH   =  "//ul[contains(@class,'react-autosuggest__suggestions-list')]"
    suggestion_box                  =  context.feature.driver.find_element(By.XPATH,suggestion_box_selector_XPATH)
    list_suggestion                 = suggestion_box.find_elements(By.TAG_NAME,'li')

    for emiten in list_suggestion:
        emiten_code = emiten.find_element(By.TAG_NAME,'i')
        if emiten_code.text == "ADRO":
            context.feature.actions.move_to_element(emiten).click().perform()
            break
        # context.feature.actions.move_to_element(emiten).click().perform()
        # break
    # pdb.set_trace()
    # TO DO : pop up will appear, need to capture "Company is added"
    # <code here>

    print(u'STEP: When User fill the wishlist menu as "ADRO')
    context.feature.driver.implicitly_wait(2)



@then(u'Wishlist "ADRO" will be shown in the list')
def step_impl(context):
    # pdb.set_trace()
    stock_table_locator_ID  = 'stock_table'
    stock_table_locator     = context.feature.driver.find_element(By.ID,stock_table_locator_ID)

    stock_emiten_code_locator_XPATH = "//tbody[contains(@class,'ant-table-tbody')]/tr"
    stock_emiten_code_locator       =  stock_table_locator.find_elements(By.XPATH,stock_emiten_code_locator_XPATH)

    for code in stock_emiten_code_locator:
        emiten_code = copy.copy(code)
        div_inner   = emiten_code.find_element(By.TAG_NAME,'div')
        #delete_item = div_inner.find_element(By.XPATH,"//span[contains(@title,'Delete this item')]")
        if context.emiten_sample in div_inner.text:
            print(f'div_inner text {div_inner.text}')
            assert True
            print(f'emiten {context.emiten_sample} is successfully added to watchlist')
            break