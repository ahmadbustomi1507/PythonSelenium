
import sys
sys.path.insert('.')

def driver_path(chrome_version=''):
    # TO DO : add if else environtment, which one of chrome version to be used
    driver_path = ".\ChromeWebdriver\97.0.4692.71\chromedriver.exe"
    # driver_path = ".\ChromeWebdriver\96.0.4664.45\chromedriver.exe"
    # driver_path = ".\ChromeWebdriver\95.0.4638.69\chromedriver.exe"
    return driver_path