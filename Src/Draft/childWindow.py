from selenium import webdriver

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()

#property window_handles is an attribute
(Parent_ID,Child_ID)=driver.window_handles


driver.switch_to.window(Child_ID)
print(driver.find_element_by_tag_name('h3').text)
driver.close()
driver.switch_to.window(Parent_ID)

