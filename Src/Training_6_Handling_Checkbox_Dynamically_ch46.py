from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# use common element that is used by all of them, in this case "type"
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()

        #to validate if its selected or not
        assert checkbox.is_selected()
    else:
        assert checkbox.is_selected() == False
