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
- tagName

'''

from selenium import webdriver
PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)


#css selector , tag[attribute = value]
#xpath selector , //tag[@attribute=value]
driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element_by_css_selector("input[name='name']").send_keys('Tomi')
driver.find_element_by_xpath("//input[@type='submit']").click()

# extracting text with different selector
print(driver.find_element_by_class_name("alert-success").text)

# css with regex (using star '*')
print(driver.find_element_by_css_selector("div[class*='alert-success']").text)

# xpath with regex (using contains)
print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)

#generating CSS from id tagname#id
#driver.find_element_by_css_selector("input#username")

#driver.find_element_by_link_text("Forgot Your Password?").click()