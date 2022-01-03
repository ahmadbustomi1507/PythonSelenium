from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/iframe")

# frame id or frame name or index value
driver.switch_to.frame('mce_0_ifr')
driver.find_element_by_css_selector('#tinymce').clear()
driver.find_element_by_css_selector('#tinymce').send_keys('i am able to automate')
driver.switch_to.default_content()
print(driver.find_element_by_tag_name('h3').text)