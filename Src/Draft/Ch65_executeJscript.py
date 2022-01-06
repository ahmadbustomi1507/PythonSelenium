#java script executor
# accessing DOM document object model

from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://rahulshettyacademy.com/AutomationPractice")


driver.find_element_by_name('name').send_keys('hello')
driver.execute_script('return document.getElementsByName("name")[0].value')




