'''
html -> tag, attribute, attribute value, content

<a href ="hope.html">computer hope</a>


Webdriver locators
- ID findElementByID
- Name
- Xpath
- Css
- ClassName
- linkText

'''
# import os
# os.environ['VIRTUAL_ENV']


from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element_by_name("name").send_keys("Rahul")
