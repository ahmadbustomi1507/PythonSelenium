
from selenium import webdriver
PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://login.salesforce.com")

#generating CSS from id tagname#id
driver.find_element_by_css_selector("input#username").send_keys("Tomi")

#generating CSS from classname  tagname.classname
# driver.find_element_by_css_selector("input.password").send_keys("Tomi")
# driver.find_element_by_css_selector("input.password").clear()

#getting linktext in anchor tag
driver.find_element_by_link_text("Forgot Your Password?").click()

#generating xpath based on text
#driver.find_element_by_xpath("//input[text()='Cancel']").click()
driver.find_element_by_xpath("//input[@type='button']").click()


#creating xpath and css by traverse tags
# in xpath => parent/child          ex: //div[@id='username']/label
# in css => parent<space>child      ex: div[id='username'] label

# in xpath => grandparent/parent/child  ex: //div[@id='username']/div[1]/label
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)


# in css => parent<space>child      ex: div[id='username'] label
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)


