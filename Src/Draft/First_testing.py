from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get('https://www.python.org/')
print(driver.current_url)

driver.close()
