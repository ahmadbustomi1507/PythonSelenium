from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(PATH)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)

#root
countries =driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li")
#[print(x) for x in countries]
for country in countries:
    #cara 1
    #child_tag = country.find_element_by_css_selector('li>a')

    #cara 2 = xpath harus dari parentsnya
    child_tag = country.find_element_by_xpath('//li[contains(@class,"ui-menu-item")]/a')

    print("id_attribute :{}".format(child_tag.get_attribute('id')) )
    print("text_attribute :{}".format(child_tag.text) )

#for country in countries:
    # print('country:{}'.format(country))
    # print('get attribute:{}'.format(country.get_attribute('li')))
 #   country.find_element_by_tag_name('li')
  #  print(A)
# print(countries)
# print(countries.get_attribute('ui-id-42'))

# for country in countries:
#     print(country.text)
#     if country.text == "India":
#         country.click()
#         break
#
# assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"

