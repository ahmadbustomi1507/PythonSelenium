
from selenium import webdriver
#from selenium.webdriver.support.select import  Select
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--enable-gpu")

PATH      = "E:\Training\Selenium-Python\chromedriver_win32\chromedriver.exe"
driver    = webdriver.Chrome(executable_path=PATH,options=chrome_options)

start = time.time()

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element_by_name("name").send_keys("Rahul")

end = time.time()
duration = end - start

print('start = {}'.format(start))
print('end = {}'.format(end))
print('duration = {}'.format(duration))

