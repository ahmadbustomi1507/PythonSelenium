from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

#please check your google chrome version, and uncomment one of these driver_path

#If you are using Chrome version 97
driver_path = "../tools/ChromeWebdriver/97.0.4692.71/chromedriver.exe"

# If you are using Chrome version 96
# driver_path = "..\ChromeWebdriver\96.0.4664.45\chromedriver.exe"

# If you are using Chrome version 95
# driver_path = "..\ChromeWebdriver\95.0.4638.69\chromedriver.exe"


driver      = webdriver.Chrome(executable_path=driver_path)


driver.get("https://zzzscore.com/1to50/en/")

for i in range(0,50):
    number = "//div[text()='{}']".format(i+1)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, number))
        )
    finally:
        driver.find_element_by_xpath(number).click()
        logging.info("\'{}\' was found".format(number))

#==================================
# Forcely disabled the ads
#==================================

#driver.execute_script('''
#
# var elems = document.getElementsByTagName("iframe");
# for(var i = 0, max = elems.length; i < max; i++)
#          {
#              elems[i].style='display: none';
#              }
# ''')

score = driver.find_element_by_id('time').text
logging.info('Your final score is {} sec'.format(score))

driver.quit()



