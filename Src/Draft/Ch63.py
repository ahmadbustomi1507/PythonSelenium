from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

action = webdriver.ActionChains(driver)

menu        = driver.find_element_by_id("mousehover")
action.move_to_element("menu").perform()
child_menu  = driver.find_element_by_link_text("Top")
action.move_to_element(child_menu).click().perform()