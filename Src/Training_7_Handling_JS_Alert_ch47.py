from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# use common element that is used by all of them, in this case "type"
driver.find_element_by_css_selector("#name").send_keys('button3')
driver.find_element_by_id("alertbtn").click()

#switch to alert
alert = driver.switch_to.alert
print(alert.text)
alert.accept()


alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()
