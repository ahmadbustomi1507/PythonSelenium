
from selenium import webdriver
from selenium.webdriver.support import select

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("input[name='name']").send_keys('Tomi')


#select class provide the methods to handle the options in dropdown
gender_selector = driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']")
dropdown        = select.Select(gender_selector)

dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0) #Male
#dropdown.select_by_value("Female")

